"""
fbmarketplace index (main) view.

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

@fbmarketplace.app.route('/api/v1/', methods=["GET"])
def get_resources():
    """Return resources."""
    if "username" not in flask.session:
        flask.abort(403)

    context = {}
    # posts
    context["posts"] = "/api/v1/p/"
    # url
    context["url"] = flask.request.path

    return flask.jsonify(**context)
