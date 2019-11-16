
# Flask_Base:

#### It's a MVT structure to start developing web applications based on [Flask](http://flask.pocoo.org/docs/0.12/). The structure is improved to work with **PostgreSQL**, but you can also work with any other [RDBMS](https://en.wikipedia.org/wiki/Relational_database#RDBMS).

---

  
  

### Git Clone and Deploy:

#### To start working with it you must clone this repository and provide a optimal [virtualenvironment](https://wiki.archlinux.org/index.php/Python/Virtual_environment) in order to deploy *Flask_Base*. It's important to install *virtualenvwrapper* on your system, it's a great tool to manage virtualenv.

#### Your system must have Postgresql installed, and the following packages will be required:
```
postgresql-11 libpq-dev python3-dev
```
<br>

  ### Remember:
  You must configure a **user** and a **database** for your application on PostgreSQL!

---

  <br>
  
After you've installed those system dependencies, you can proceed cloning ***Flask_Base***:
```

# git clone http://github.com/MarcelFox/flask_base

# cd flask_base/

# mkvirtualenv --python="/usr/bin/python3" -r requirements.txt venv_name

```

  

<br  />


#### This flask base structure uses [environment variables](https://stackoverflow.com/a/11134336/8077923) which works very well with *virtualenvwrapper*. At this point we have to set up only two variables:

  

`SECRET_KEY`

`DATABASE_URL`

  

<br  />
  

#### Just add the following lines into the *postactivate* file on your virtualenv:

  

`$HOME/.virtualenvs/venv_name/bin/postactivate:`

  

```

export FLASK_APP='$HOME/flask_base/run.py'

export SECRET_KEY='Shrubbery'

export DATABASE_URL='postgresql://USER:PASS@localhost/DATABASE'

```

  

<br  />

  

#### You also need to unset these variables when you *deactivate* from your virtualenv:

`$HOME/.virtualenvs/venv_name/bin/postdeactivate:`

```

unset FLASK_APP

unset SECRET_KEY

unset DATABASE_URL

```

<br  />


### Run!
uwsgi --ini="uwsgi.ini"

Now your application will be accessible on:
http://localhost:8080/