from flask import render_template, flash, redirect, url_for, request 
from flask_base import app
from flask_base.models import Profile, login_manager
from flask_base.forms import LoginForm
from flask_login import login_user, login_required, logout_user, current_user
from datetime import timedelta

#   a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'


# @app.route('/')
# def index():
#     return render_template(
#         'index.html',
#         hello="Hello You!",  # Jinja2 working variables
#         # check the index.html who is {{ hello }} =)
#         user=current_user
#     )


@app.route('/login', methods=['GET', 'POST'])
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



@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template(
    'admin.html',
    title = 'Admin',
    user = current_user
    )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
