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

@fbmarketplace.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Return resources."""
    context = {}
    # posts
    context["posts"] = "/api/v1/p/"
    # url
    context["url"] = flask.request.path

    return flask.jsonify(**context)
