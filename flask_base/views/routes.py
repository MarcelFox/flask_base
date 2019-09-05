
from datetime import timedelta
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from forms import LoginForm
from .models import Profile

# !!! 'routes' is a ugly name, the correct is to separate all of those routes into their own files
routes = Blueprint('routes', __name__)


#   a simple page that says hello
@routes.route('/')
def hello():
    return 'Hello, World!'


@routes.route('/')
def index():
    return render_template(
        'index.html',
        hello="Hello You!",  # Jinja2 working variables
        # check the index.html who is {{ hello }} =)
        user=current_user
    )


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Profile.query.filter_by(username=form.username.data).first()

        if form.remember is True:
            login_user(user, remember=True, duration=timedelta(minutes=30))
        else:
            login_user(user)

        return redirect(url_for('admin'))

    return render_template(
        'login.html',
        title='Sign In',
        form=form
    )



@routes.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template(
    'admin.html',
    title = 'Admin',
    user = current_user
    )

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
