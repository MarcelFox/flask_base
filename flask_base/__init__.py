from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    from . import views, models

    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    with app.app_context():
        from .views import routes

        db.create_all()

        return app
