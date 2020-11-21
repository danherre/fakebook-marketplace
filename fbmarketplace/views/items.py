import os
import shutil
import tempfile
import hashlib
import flask
import fbmarketplace
from fbmarketplace.model import get_db

#  ------- Feed -------  #
@fbmarketplace.app.route('/', methods=['GET'])
def index():
    #if 'username' not in flask.session:
        #return flask.redirect(flask.url_for('login'))

    data = {}
    #data["username"] = flask.session['username']

    cursor = get_db().execute('''SELECT * FROM items ORDER BY itemid DESC LIMIT 8''')
    item_dict = cursor.fetchall()
    item_list = []
    for item in item_dict:
        owner = item["owner"]

        cursor = get_db().execute('''SELECT fullname FROM users
            WHERE username = '%s' ''' % owner)
        fullname = cursor.fetchone()
        item["fullname"] = fullname["fullname"]

        cursor = get_db().execute('''SELECT filename FROM users
            WHERE username = '%s' ''' % owner)
        filename = cursor.fetchone()
        item["owner_img"] = filename["filename"]

        cursor = get_db().execute('''SELECT rating FROM reviews
            WHERE writee = '%s' ''' % owner)
        rating = cursor.fetchall()
        sum = 0
        num = 0
        for rate in rating:
            num += 1
            sum += rate["rating"]
        item["rating"] = sum/num

        item_list.append(item)

    data["items"] = item_list

    return flask.jsonify(**data)

#  ------- Search -------  #
@fbmarketplace.app.route('/search/', methods=['GET'])
def search():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    data = {}
    data["username"] = flask.session['username']

    item_list = []
    if flask.request.args.get('search') is not None:
        search = flask.request.args.get('search')
        data["search"] = search
        cursor = get_db().execute("SELECT * FROM items WHERE name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' ORDER BY itemid DESC LIMIT 8")
        item_dict = cursor.fetchall()
        for item in item_dict:
            owner = item["owner"]

            cursor = get_db().execute('''SELECT fullname FROM users
                WHERE username = '%s' ''' % owner)
            fullname = cursor.fetchone()
            item["fullname"] = fullname["fullname"]

            cursor = get_db().execute('''SELECT filename FROM users
                WHERE username = '%s' ''' % owner)
            filename = cursor.fetchone()
            item["owner_img"] = filename["filename"]

            cursor = get_db().execute('''SELECT rating FROM reviews
                WHERE writee = '%s' ''' % owner)
            rating = cursor.fetchall()
            sum = 0
            num = 0
            for rate in rating:
                num += 1
                sum += rate["rating"]
            item["rating"] = sum/num

            item_list.append(item)

    data["items"] = item_list

    return flask.render_template("search.html", **data)

#  ------- Category Search -------  #
@fbmarketplace.app.route('/categories/<category>/', methods=['GET'])
def category_search(category):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    data = {}
    data["username"] = flask.session['username']

    cursor = get_db().execute('''SELECT * FROM items WHERE category = '%s' ORDER BY itemid DESC LIMIT 8''' % category)
    item_dict = cursor.fetchall()
    item_list = []
    for item in item_dict:
        owner = item["owner"]

        cursor = get_db().execute('''SELECT fullname FROM users
            WHERE username = '%s' ''' % owner)
        fullname = cursor.fetchone()
        item["fullname"] = fullname["fullname"]

        cursor = get_db().execute('''SELECT filename FROM users
            WHERE username = '%s' ''' % owner)
        filename = cursor.fetchone()
        item["owner_img"] = filename["filename"]

        cursor = get_db().execute('''SELECT rating FROM reviews
            WHERE writee = '%s' ''' % owner)
        rating = cursor.fetchall()
        sum = 0
        num = 0
        for rate in rating:
            num += 1
            sum += rate["rating"]
        item["rating"] = sum/num

        item_list.append(item)

    data["items"] = item_list

    return flask.render_template("categories.html", **data)
