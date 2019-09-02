
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_base import models, views

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db = SQLAlchemy(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    # a simple page that says hello
    # @app.route('/')
    # def hello():
    #     return 'Hello, World!'

    return app
    