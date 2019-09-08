from .base import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


admin = User(username='admin', email='admin@example.com',
             password='coconuts')


def init_app(app):
    db.init_app(app)
    with app.app_context():
        user = User.query.filter_by(username='admin').first()
        if user is None:
            db.session.add(admin)
            db.session.commit()
        db.create_all()
        app.logger.info('itsworks')

