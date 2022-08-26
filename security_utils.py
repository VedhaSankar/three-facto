from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

def hash_password(password):

    return bcrypt.generate_password_hash(password)

def match_password(db_password, password):

    return bcrypt.check_password_hash(db_password, password)

def set_password(pw):

    pwhash = bcrypt.generate_password_hash(pw.encode('utf8'))
    password_hash = pwhash.decode('utf8')

    return password_hash