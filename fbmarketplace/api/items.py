import flask
from flask import session, abort
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
def get_items_by_user(username):
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
        if 'image' in flask.request.files:
            image = flask.request.files['image']
            filename = sha256sum(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flask.request.form['description']

    return flask.jsonify(**response)
