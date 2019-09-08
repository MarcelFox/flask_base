
def init_app(app):
    from . import User
    User.init_app(app)