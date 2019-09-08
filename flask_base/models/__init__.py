
def init_app(app):
    from .base import db
    from .User import User

    admin = User(username='admin', email='admin@example.com',
                 password='coconuts')

    db.init_app(app)

    with app.app_context():
        user = User.query.filter_by(username='admin').first()
        if user is None:
            db.session.add(admin)
            db.session.commit()
        db.create_all()
