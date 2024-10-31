from flask import Flask
from .target.dash import target
from .login_manager_setup import login_manager

def create_app(config_name):
    # ..
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    login_manager.init_app(app)

    app.register_blueprint(target)
    # .. 
    return app