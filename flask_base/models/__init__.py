
# models.__init__.py

from . import base

def init_app(app):
    from flask_login import LoginManager
    db = base.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    return db