from base_app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Profile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    surName = db.Column(db.String(100), nullable=False)
    description = db.Column (db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

# Create Tables into our database:
db.create_all()


# Add some information:
DummyData = Profile(
    username = 'Tester',
    password = generate_password_hash('1q2w3e4r'),
    firstName='Test',
    surName='User',
    description='I am a dummy data on your database',
    email='test@uwsgi.dom',
)


# Check if DummyData exists, if not, insert the DummyData content:
if Profile.query.filter_by(email='test@uwsgi.dom').first() is None:
    db.session.add(DummyData)
    db.session.commit()

# Query a specific username from 'Profile' table:
q_var = Profile.query.filter_by(username='Tester').first()

# Now we can check 'username', 'password' and so forth:
# q_var.username, q_var.password ...
#
# For instance, you can check if the password is correct by using:
# check_password_hash(q_var.password, '1q2w3e4r')
