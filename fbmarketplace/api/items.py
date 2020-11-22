import flask
from flask import session, abort
import tempfile
import shutil
import os
import fbmarketplace
from fbmarketplace.api.hashing import sha256sum

def get_item_data(line):
    """Translate the database output for a post into a dictionary."""
    response = {}
    response['itemid'] = int(line['itemid'])
    response['owner'] = line['owner']
    response['name'] = line['name']
    response['description'] = line['description']
    response['price'] = float(line['price'])
    response['image'] = line['image']
    response['posted'] = line['posted']
    response['available'] = bool(line['available'])
    return response

def get_review_data(line):
    """Translate the database output for a post into a dictionary."""
    response = {}
    response['reviewid'] = int(line['reviewid'])
    response['writer'] = line['writer']
    response['writee'] = line['writee']
    response['review'] = line['review']
    response['created'] = line['created']
    response['rating'] = line['rating']
    return response 

@fbmarketplace.app.route('/api/items/', methods=['GET'])
def get_items():
    connection = fbmarketplace.model.get_db()
    page = flask.request.args.get("page", default=0, type=int)
    response = {}
    if flask.request.args.get('search') is not None:
        search = flask.request.args.get('search')
        cur = connection.execute(
            "SELECT * FROM items WHERE name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' LIMIT 4 OFFSET " + str(4*page)
        )
        items = cur.fetchall()
        response['results'] = [get_item_data(item) for item in items]
        if flask.request.args.get("page") is None:
            page = 0
        response['next'] = '/api/items/?page=' + str(page+1) + '&search=' + search
    else: 
        cur = connection.execute(
            "SELECT * FROM items ORDER BY itemid DESC LIMIT 4 OFFSET " + str(4*page)
        )
        items = cur.fetchall()
        response['results'] = [get_item_data(item) for item in items]
        if flask.request.args.get("page") is None:
            page = 0
        response['next'] = '/api/items/?page=' + str(page+1)

    return flask.jsonify(**response)


@fbmarketplace.app.route('/api/items/<username>/', methods=['GET', 'POST'])
def items_by_user(username):
    connection = fbmarketplace.model.get_db()
    response = {}
    if flask.request.method=='GET':
        page = flask.request.args.get("page", default=0, type=int)
        cur = connection.execute(
            "SELECT * FROM items WHERE owner='" + username + "' ORDER BY itemid DESC LIMIT 4 OFFSET " + str(4*page)
        )
        items = cur.fetchall()
        response['results'] = [get_item_data(item) for item in items]
        if flask.request.args.get("page") is None:
            page = 0
        response['next'] = '/api/items/' + username + '/?page=' + str(page+1)
    else: # TODO: Figure out how to save file
        if "username" not in flask.session:
            abort(403)
        if "create_post" in flask.request.form:
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
            response['Success'] = True
        else: #delete a post
            cur = connection.execute(
                "SELECT owner FROM items WHERE itemid='" + flask.request.form['itemid'] + "'"
            )
            owner = cur.fetchone()['owner']
            if owner != flask.session['username']:
                abort(403)
            cur = connection.execute(
                "DELETE FROM items WHERE itemid='" + flask.request.form['itemid'] + "'"
            )
            response['Success'] = True
    return flask.jsonify(**response)


@fbmarketplace.app.route('/api/reviews/<username>/', methods=['GET', 'POST'])
def reviews_by_user(username):
    connection = fbmarketplace.model.get_db()
    response = {}
    # if GET request, return 4 newest reviews of user
    if flask.request.method=='GET':
        page = flask.request.args.get("page", default=0, type=int)
        cur = connection.execute(
            "SELECT * FROM reviews WHERE writee='" + username + "' ORDER BY reviewid DESC LIMIT 4 OFFSET " + str(4*page)
        )
        items = cur.fetchall()
        response['results'] = [get_review_data(item) for item in items]
        if flask.request.args.get("page") is None:
            page = 0
        response['next'] = '/api/reviews/' + username + '/?page=' + str(page+1)
    else: 
        if "username" not in flask.session:
            abort(403)
        cur = connection.execute(
            "INSERT INTO reviews (writer, writee, review, rating) VALUES ('" + 
            flask.session['username'] + "', '" + 
            username + "', '" + 
            flask.request.form['review'] + "', '" + 
            flask.request.form['rating'] + "')"
        )
        response['Success'] = True
    return flask.jsonify(**response)    