
import os, sys

try: 
    SECRET_KEY = os.environ['SECRET_KEY']
except:
    print("\nERROR: You must set the 'SECRET_KEY' evironment variable on your virtualenv.\n")
    sys.exit(1)

try:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
except:
    print("\nERROR: You must set the 'DATABASE_URL' evironment variable on your virtualenv.\n")
    sys.exit(1)
    # Advice: export DATABASE_URL='postgresql://USER:PASS@localhost/DATABASE'


SQLALCHEMY_TRACK_MODIFICATIONS='False'