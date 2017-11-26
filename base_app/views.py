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
    return render_template(
	'login.html',
	title ='Sign In',
	form = form
	)

