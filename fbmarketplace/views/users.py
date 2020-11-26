import os
import shutil
import tempfile
import hashlib
import flask
from flask import session, abort
import fbmarketplace
from fbmarketplace.api.hashing import sha256sum
from fbmarketplace.model import get_db

@fbmarketplace.app.route('/u/<username>/', methods=['GET', 'POST'])
def user(username):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    response = {}
    response['logname'] = flask.session['username']
    response['username'] = username

    connection = fbmarketplace.model.get_db()

    if flask.request.method == 'POST':
        if "create_post" in flask.request.form:
            if response['logname'] != response['username']:
                abort(403)
            dummy, temp_filename = tempfile.mkstemp()
            image = flask.request.files['image']
            image.save(temp_filename)
            hash_txt = sha256sum(temp_filename)
            dummy, suffix = os.path.splitext(image.filename)
            hash_filename_basename = hash_txt + suffix
            hash_filename = os.path.join(
                fbmarketplace.app.config["UPLOAD_FOLDER"],
                hash_filename_basename
            )
            shutil.move(temp_filename, hash_filename)
            cur = connection.execute(
                "INSERT INTO items (owner, name, description, price, available, image) VALUES ('" +
                username + "', " +
                flask.request.form['name'] + "', '" +
                flask.request.form['description'] + "', '" +
                flask.request.form['price'] + "', '" +
                flask.request.form['available'] + "', '" +
                hash_filename_basename + "')"
            )
        elif "delete_post" in flask.request.form: #delete a post
            if response['logname'] != response['username']:
                abort(403)
            cur = connection.execute(
                "SELECT owner FROM items WHERE itemid='" + flask.request.form['itemid'] + "'"
            )
            owner = cur.fetchone()['owner']
            if owner != flask.session['username']:
                abort(403)
            cur = connection.execute(
                "DELETE FROM items WHERE itemid='" + flask.request.form['itemid'] + "'"
            )
        elif "post_review" in flask.request.form:
            if response['logname'] == response['username']:
                abort(403)
            cur = connection.execute(
                "INSERT INTO reviews (writer, writee, review, rating) VALUES ('" +
                response['logname'] + "', '" +
                response['username'] + "', '" +
                flask.request.form['review'] + "', '" +
                flask.request.form['rating'] + "')"
            )
    cur = connection.execute(
        "SELECT * FROM users WHERE username='" + username + ""
    )
    user = cur.fetchall()
    response['user'] = user
    cur = connection.execute(
        "SELECT * FROM items WHERE owner='" + username + "' ORDER BY itemid DESC"
    )
    items = cur.fetchall()
    response['items'] = items
    cur = connection.execute(
        "SELECT * FROM reviews WHERE writee='" + username + "' ORDER BY reviewid DESC"
    )
    reviews = cur.fetchall()
    response['reviews'] = reviews
    sum = 0
    for review in reviews:
        sum += review['rating']
    avg = sum / len(reviews)
    response['average_rating'] = avg
    return flask.render_template("user.html", **response)
