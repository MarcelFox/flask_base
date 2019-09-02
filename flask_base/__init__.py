
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


#def create_app(test_config=None):
# def create_app():
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object('config')

#     # @app.route('/')
#     # def hello():
#     #     return 'Hello, World!'


#     @app.route('/')
#     def index():
#         return 'heloo'

#     return app

app = Flask('__name__')
app.config.from_object('config')

from flask_base import models, views
