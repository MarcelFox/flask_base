from flask import Blueprint, render_template
from flask import current_app as app
from App import db
from App.models.User import User


index = Blueprint('index', __name__)

@index.route('/')
def main_page():

    def createUser():
        admin = User(username='admin',
                    email='admin@example.com',
                    password='coconuts')
        # app.logger.info("[ADMIN]: " + admin.username)
        db.session.add(admin)
        db.session.commit()

    user = User.query.filter_by(username='admin').first()
    if user is None:
        createUser()
        
        
    return render_template('index.html', user=user)


app.register_blueprint(index)