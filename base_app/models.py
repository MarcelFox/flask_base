from base_app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Profile.query.get(int(user_id))


class Profile(db.Model, UserMixin):

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
    username = 'tester1',
    password = generate_password_hash('1q2w3e4r'),
    firstName='Test1_first_name',
    surName='Test1_sur_name',
    description='I am the first dummy data on your database',
    email='test1@uwsgi.dom',
)


# Check if DummyData exists, if not, insert the DummyData content:
if Profile.query.filter_by(email='test1@uwsgi.dom').first() is None:
    db.session.add(DummyData)
    db.session.commit()

# Query a specific username from 'Profile' table:
q_var = Profile.query.filter_by(username='Tester').first()

# Now we can check 'username', 'password' and so forth:
# q_var.username, q_var.password ...
#
# For instance, you can check if the password is correct by using:
# check_password_hash(q_var.password, '1q2w3e4r')


DummyData2 = Profile(
    username = 'tester2',
    password = generate_password_hash('1q2w3e4r'),
    firstName='Test2_first_name',
    surName='Test2_sur_name',
    description='I am the second dummy data on your database',
    email='test2@uwsgi.dom',
)

if Profile.query.filter_by(email='test2@uwsgi.dom').first() is None:
    db.session.add(DummyData2)
    db.session.commit()

