# from flask import Flask, render_template, redirect, url_for, request
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#   return render_template('index.html')
#
# @app.route('/save', methods=['POST'])
# def ssave():
#   return redirect(url_for('index'))
# app.run(debug=True, host='0.0.0.0', port=8080)
#
# request.
# from flask import Flask, make_response
#
# app = Flask(__name__)
#
#
# @app.route('/save')
# def save():
#     response = make_response()
#     response.set_cookie('treehouse', 'treehouse')


from flask.ext.bcrypt import generate_password_hash, check_password_hash

def set_password(User, pw):
    hash_pw = generate_password_hash('pw')
    User.password = hash_pw
    return User

def validate_password(user, pw):
    hash_pw = set_password(user, pw)
    unhash_pw = check_password_hash(hash_pw, pw)
    if unhash_pw is True:
        print('True')
        return True
    else:
        print('False')
        return False