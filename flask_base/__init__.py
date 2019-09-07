from flask import Flask

def create_app():
    from .views.routes import index
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(index)
    return app