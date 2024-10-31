#from flask import render_template, redirect, request, url_for, flash
#from flask_login import login_user
'''
from . import auth
from ..models import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me', False)
        user = User.objects(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user, force=True)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
    return render_template('auth/login.html')
