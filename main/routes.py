'''
from . import main
from flask import Blueprint, render_template
from flask_login import login_required


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')