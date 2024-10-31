from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import current_user, fresh_login_required

target = Blueprint('target', __name__)

@target.route('/dashboard', methods=['GET', 'POST'])
@fresh_login_required
def dashboard():
    if current_user.is_authenticated:
        ...
        return render_template('dashboard.html')
    else:
        session['dest_url']=request.endpoint
        return redirect(url_for('app.login'))