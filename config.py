import os, sys, logging

logging.basicConfig(filename='info.log', format='%(pathname)s at line %(lineno)d: %(message)s', level=logging.INFO)
logging.StreamHandler(stream=sys.stdout)

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


SQLALCHEMY_TRACK_MODIFICATIONS = False

TEMPLATES_AUTO_RELOAD = True
