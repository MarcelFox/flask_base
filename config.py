# Remember to use a JSON file instead.
# Remember to inform about virtualenv environment variables.

import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))


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

RECAPTCHA_PUBLIC_KEY='6LdgKAMTAAAAAOmWfxKe1XoVih_W-JatCVsC2ML6'
RECAPTCHA_PRIVATE_KEY='6LdgKAMTAAAAAE5YVbCJ5GGLGDWj1mzFrZhztJix'
