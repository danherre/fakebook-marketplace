import os
import shutil
import tempfile
import hashlib
import flask
import fbmarketplace
from fbmarketplace.model import get_db

def sha256sum(filename):
    """Return sha256 hash of file content, similar to UNIX sha256sum."""
    content = open(filename, 'rb').read()
    sha256_obj = hashlib.sha256(content)
    return sha256_obj.hexdigest()

#  ------- Login -------  #
@fbmarketplace.app.route('/accounts/login/', methods=['GET', 'POST'])
def login():
    """Render login."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('index'))

    if flask.request.method == 'POST':
        entered_username = flask.request.form['username']
        entered_password = flask.request.form['password']

        # check if username exists
        cursor = get_db().execute('''SELECT * FROM users WHERE username
                    = '%s' ''' % entered_username)
        user_dict = cursor.fetchall()
        if len(user_dict) != 1:
            return flask.redirect(flask.url_for('login'))

        # check if password matches
        used_salt = user_dict[0]['password']
        used_salt = used_salt.split('$')[1]
        used_salt = used_salt.split('$')[0]
        algorithm = 'sha512'
        hash_obj = hashlib.new(algorithm)
        password_salted = used_salt + entered_password
        hash_obj.update(password_salted.encode('utf-8'))
        password_hash = hash_obj.hexdigest()
        password_db_string = "$".join([algorithm, used_salt,
                                       password_hash])
        if user_dict[0]['password'] != password_db_string:
            return flask.redirect(flask.url_for('login'))

        flask.session['username'] = flask.request.form['username']
        return flask.redirect(flask.url_for('index'))
    data = {}
    return flask.render_template("login.html", **data)


#  ------- Logout -------  #
@fbmarketplace.app.route('/accounts/logout/')
def logout():
    """Render logout."""
    flask.session.clear()
    return flask.redirect(flask.url_for('login'))

#  ------- Create Account -------  #
@fbmarketplace.app.route('/accounts/create/', methods=['GET', 'POST'])
def create():
    """Render create."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('edit'))

    if flask.request.method == 'POST':
        # check if username exists
        cursor = get_db().execute('''SELECT * FROM users WHERE username
                                  = '%s' ''' % flask.request.form['username'])
        user_dict = cursor.fetchall()
        if user_dict:
            flask.abort(409)

        # check if password is not empty
        if flask.request.form['password'] == "":
            flask.abort(400)

        # format file
        # Save POST request's file object to a temp file
        dummy, temp_filename = tempfile.mkstemp()
        file = flask.request.files["file"]
        file.save(temp_filename)

        # Compute filename
        hash_txt = sha256sum(temp_filename)
        dummy, suffix = os.path.splitext(file.filename)
        hash_filename = os.path.join(
            insta485.app.config["UPLOAD_FOLDER"],
            hash_txt + suffix
        )

        # Move temp file to permanent location
        shutil.move(temp_filename, hash_filename)

        # hash password
        algorithm = 'sha512'
        salt = uuid.uuid4().hex
        hash_obj = hashlib.new(algorithm)
        password_salted = salt + flask.request.form['password']
        hash_obj.update(password_salted.encode('utf-8'))
        password_hash = hash_obj.hexdigest()

        cursor = get_db().execute('''INSERT INTO
                                     users(username, fullname, email,
                                     filename, password, rating)
                                     VALUES ('%s', '%s', '%s', '%s', '%s', %d)'''
                                  % (flask.request.form['username'],
                                     flask.request.form['fullname'],
                                     flask.request.form['email'],
                                     hash_txt + suffix,
                                     "$".join([algorithm, salt,
                                               password_hash]), 0.0))
        flask.session['username'] = flask.request.form['username']
        return flask.redirect(flask.url_for('index'))
    data = {}
    return flask.render_template("create.html", **data)


#  ------- Delete Account -------  #
@fbmarketplace.app.route('/accounts/delete/', methods=['GET', 'POST'])
def delete():
    """Render delete."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    if flask.request.method == 'POST':
        cursor = get_db().execute('''SELECT * FROM items WHERE owner = '%s' '''
                                  % flask.session['username'])
        item_dict = cursor.fetchall()
        for items in item_dict:
            item = items['filename']
            os.remove(os.path.join(fbmarketplace.app.config["UPLOAD_FOLDER"], item))
        cursor = get_db().execute('''SELECT * FROM users WHERE username = '%s'
                                  ''' % flask.session['username'])
        user_dict = cursor.fetchall()
        os.remove(os.path.join(fbmarketplace.app.config["UPLOAD_FOLDER"],
                               user_dict[0]['filename']))
        cursor = get_db().execute('''DELETE FROM users WHERE username
                                  = '%s' ''' % flask.session['username'])
        flask.session.clear()
        return flask.redirect(flask.url_for('create'))
    data = {
        "logname": flask.session['username']
    }
    return flask.render_template("delete.html", **data)


#  ------- Edit Account -------  #
@fbmarketplace.app.route('/accounts/edit/', methods=['GET', 'POST'])
def edit():
    """Render edit."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    if flask.request.method == 'POST':
        if 'file' in flask.request.files:
            # format file
            # Save POST request's file object to a temp file
            dummy, temp_filename = tempfile.mkstemp()
            file = flask.request.files["file"]
            file.save(temp_filename)

            # Compute filename
            hash_txt = sha256sum(temp_filename)
            dummy, suffix = os.path.splitext(file.filename)
            hash_filename_basename = hash_txt + suffix
            hash_filename = os.path.join(
                fbmarketplace.app.config["UPLOAD_FOLDER"],
                hash_filename_basename
            )
            # Move temp file to permanent location
            shutil.move(temp_filename, hash_filename)
            cursor = get_db().execute('''UPDATE users SET filename = '%s',
                                         fullname = '%s', email = '%s'
                                         WHERE username = '%s' '''
                                      % (hash_filename_basename,
                                         flask.request.form['fullname'],
                                         flask.request.form['email'],
                                         flask.session['username']))
        else:
            cursor = get_db().execute('''UPDATE users SET fullname = '%s',
                                         email = '%s' WHERE username = '%s' '''
                                      % (flask.request.form['fullname'],
                                         flask.request.form['email'],
                                         flask.session['username']))

        return flask.redirect(flask.url_for('edit'))
    cursor = get_db().execute('''SELECT * FROM users WHERE username = '%s' '''
                              % flask.session['username'])
    user_dict = cursor.fetchall()
    data = {
        "logname": flask.session['username'],
        "name": user_dict[0]['fullname'],
        "email": user_dict[0]['email'],
        "pic_url": user_dict[0]['filename']
    }
    return flask.render_template("edit.html", **data)


#  ------- Change Password -------  #
@fbmarketplace.app.route('/accounts/password/', methods=['GET', 'POST'])
def password():
    """Render password."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    if flask.request.method == 'POST':
        new_pass1 = flask.request.form['new_password1']
        new_pass2 = flask.request.form['new_password2']
        if new_pass1 != new_pass2:
            flask.abort(401)

        cursor = get_db().execute('''SELECT * FROM users
                                     WHERE username = '%s' '''
                                  % flask.session['username'])
        user_dict = cursor.fetchall()
        used_salt = user_dict[0]['password']
        used_salt = used_salt.split('$')[1]
        used_salt = used_salt.split('$')[0]
        algorithm = 'sha512'
        hash_obj = hashlib.new(algorithm)
        password_salted = used_salt + flask.request.form['password']
        hash_obj.update(password_salted.encode('utf-8'))
        password_hash = hash_obj.hexdigest()
        password_db_string = "$".join([algorithm, used_salt, password_hash])
        if user_dict[0]['password'] != password_db_string:
            flask.abort(403)

        algorithm = 'sha512'
        hash_obj = hashlib.new(algorithm)
        password_salted = used_salt + flask.request.form['new_password1']
        hash_obj.update(password_salted.encode('utf-8'))
        password_hash = hash_obj.hexdigest()
        password_db_string = "$".join([algorithm, used_salt, password_hash])

        cursor = get_db().execute('''UPDATE users SET password = '%s'
                                     WHERE username = '%s' '''
                                  % (password_db_string,
                                     flask.session['username']))
        return flask.redirect(flask.url_for('edit'))
    data = {
        "logname": flask.session['username']
    }
    return flask.render_template("password.html", **data)
