from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    app.config.from_object('config')

    @app.route('/')
    def index():
        return render_template('index.html', title='Home')

    return app