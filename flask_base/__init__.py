from flask import Flask


def create_app(config):
    from . import views, models

    app = Flask(__name__)
    app.config.from_object(config)
    models.init_app(app)
    views.init_app(app)

    return app
