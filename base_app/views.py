from flask import render_template, flash, redirect
from base_app import app
from .forms import LoginForm


@app.route('/')
def index():
    return render_template(
	'index.html',
	hello = "Hello You!"  # Jinja2 working variables
	)		      # check the index.html who is {{ hello }} =)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        return '<h1>The username is {}. The password is {}.'.format(form.username.data, form.password.data)
    return render_template(
	'login.html',
	title ='Sign In',
	form = form
	)

