# Flask_Base:
#### It's a structure to start developing web applications based on [Flask](http://flask.pocoo.org/docs/0.12/). This structure is improved to work with **postgresql**, but you can also work with any database you want.
---


### Git Clone and Deploy:
#### To start working with it you must clone this repository and provide a optimal [virtualenvironment](https://wiki.archlinux.org/index.php/Python/Virtual_environment) to deploy this base structure for Flask. You must install *virtualenvwrapper* on your system, it's a great tool to manage virtualenv. 

```
# git clone http://github.com/MarcelFox/flask_base
# cd flask_base/
# mkvirtualenv --python="/usr/bin/python3" -r requirements.txt venv_name
```

<br />

#### This flask base structure uses [environment variables](https://stackoverflow.com/a/11134336/8077923) which works very well with *virtualenvwrapper*. At this point we have to set up only two variables:

`SECRET_KEY`
`DATABASE_URL`

<br />

#### Don't worry if for some reason you do not provide one of these, the application will inform you about. To set up these, you have to add the following into *postactivate* file of your virtualenv:

`$HOME/.virtualenvs/venv_name/bin/postactivate:`

```
export FLASK_APP='$HOME/flask_base/run.py'
export SECRET_KEY='Shrubbery'
export DATABASE_URL='postgresql://USER:PASS@localhost/DATABASE'
```

<br />

#### And remember to unset these variables when you *deactivate* from your virtualenv:
`$HOME/.virtualenvs/venv_name/bin/postdeactivate:`
```
unset FLASK_APP
unset SECRET_KEY
unset DATABASE_URL
```
<br />

### Run!
#### You can run your flask base with:
```
# flask run --host 0.0.0.0 --port 8080
```
<br />

#### And check your browser: http://localhost:8080

<br />

# That's all folks!

