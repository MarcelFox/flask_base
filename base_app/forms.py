from base_app.models import Profile

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from werkzeug.security import check_password_hash

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message='A username is required.')])
    password = PasswordField('Password', validators=[InputRequired(message='A Password is required.')])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = Profile.query.filter_by(
                username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown Username')
            return False

        if not check_password_hash(user.password, self.password.data):
            self.password.errors.append('Wrong password')
            return False

        self.user = user
        return True 
