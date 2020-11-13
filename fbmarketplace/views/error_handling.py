"""
fbmarketplace error handling.

"""
import os
import shutil
import tempfile
import hashlib
import flask
#import arrow
import fbmarketplace
from fbmarketplace.model import get_db

@fbmarketplace.app.errorhandler(400)
def bad_request(error):
    """Return error message."""
    print(error)
    context = {
        "message": "Bad Request",
        "status_code": 400
    }
    return flask.jsonify(**context), 400


@fbmarketplace.app.errorhandler(403)
def forbidden(error):
    """Return error message."""
    print(error)
    context = {
        "message": "Forbidden",
        "status_code": 403
    }
    return flask.jsonify(**context), 403


@fbmarketplace.app.errorhandler(404)
def not_found(error):
    """Return error message."""
    print(error)
    context = {
        "message": "Not Found",
        "status_code": 404
    }
    return flask.jsonify(**context), 404

@fbmarketplace.app.route('/api/', methods=["GET"])
def get_resources():
    """Return resources."""
    if "username" not in flask.session:
        flask.abort(403)

    context = {}
    # posts
    context["posts"] = "/api/p/"
    # url
    context["url"] = flask.request.path

    return flask.jsonify(**context)

@fbmarketplace.app.route('/api/testusers', methods=["GET"])
def test():
    """Test."""
    context = {}

    connection = fbmarketplace.model.get_db()
    cursor = connection.execute('''SELECT * FROM users''')
    users = cursor.fetchall()

    context["data"] = users
    return flask.jsonify(**context), 201

@fbmarketplace.app.route('/api/testitems', methods=["GET"])
def testitems():
    """Test."""
    context = {}

    connection = fbmarketplace.model.get_db()
    cursor = connection.execute('''SELECT * FROM items''')
    items = cursor.fetchall()

    context["data"] = items
    return flask.jsonify(**context), 201

@fbmarketplace.app.route('/api/testreviews', methods=["GET"])
def testreviews():
    """Test."""
    context = {}

    connection = fbmarketplace.model.get_db()
    cursor = connection.execute('''SELECT * FROM reviews''')
    reviews = cursor.fetchall()

    context["data"] = reviews
    return flask.jsonify(**context), 201
