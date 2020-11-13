"""Simple hashing module."""
import hashlib


def sha256sum(filename):
    """Return sha256 hash of file content, similar to UNIX sha256sum."""
    content = open(filename, 'rb').read()
    sha256_obj = hashlib.sha256(content)
    return sha256_obj.hexdigest()


def sha512sum(password, salt):
    """Return sha512 hash of password + salt."""
    content = salt + password
    sha512_obj = hashlib.new('sha512')
    sha512_obj.update(content.encode('utf-8'))
    return sha512_obj.hexdigest()

# example
# Save POST request's file object to a temp file
# dummy, temp_filename = tempfile.mkstemp()
# file = flask.request.files["file"]
# file.save(temp_filename)
#
# # Compute filename
# hash_txt = sha256sum(temp_filename)
# dummy, suffix = os.path.splitext(file.filename)
# hash_filename_basename = hash_txt + suffix
# hash_filename = os.path.join(
#     insta485.app.config["UPLOAD_FOLDER"],
#     hash_filename_basename
# )
#
# # Move temp file to permanent location
# shutil.move(temp_filename, hash_filename)
