import flask
from flask import session, abort
import fbmarketplace
from fbmarketplace.model import get_db

@fbmarketplace.app.route('/u/<username>/', methods=['GET'])
def user(username):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    response = {}
    response["logname"] = flask.session['username']

    return flask.render_template("user.html", **response)