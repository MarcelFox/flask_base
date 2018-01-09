from base_app import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    surName = db.Column(db.String(100), nullable=False)
    description = db.Column (db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# Create Tables into our database:
db.create_all()


# Add some information:
DummyData = Profile(
    username='tester',
    firstName='Test',
    surName='User',
    description='I am a dummy data on your database',
    email='test@uwsgi.dom',
)


# Check if DummyData exists, if not, insert the DummyData content:
if Profile.query.filter_by(email='test@uwsgi.dom').first() is None:
    db.session.add(DummyData)
    db.session.commit()
