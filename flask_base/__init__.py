
# flask_base.__init__

from flask import Flask


def create_app():
    from . import models, services, views
    app = Flask(__name__)
    models.init_app(app)
    views.init_app(app)
    services.init_app(app)
    return app
