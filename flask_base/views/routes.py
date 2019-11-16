from flask import Blueprint, render_template
from flask import current_app as app
from flask_base import db
from flask_base.models.User import User


index = Blueprint('index', __name__)

@index.route('/')
def main_page():
    admin = User(username='admin',
                 email='admin@example.com',
                 password='coconuts')

    app.logger.info("[ADMIN]: " + admin.username)

    user = User.query.filter_by(username='admin').first()

    if user is None:
        db.session.add(admin)
        db.session.commit()

        
    return render_template('index.html', user=user)


app.register_blueprint(index)