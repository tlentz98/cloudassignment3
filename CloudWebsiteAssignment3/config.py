import os


class Config:
    DEBUG = True
    # session secret key
    SECRET_KEY = os.urandom(12)
    # Gets pwd and declares it is the root dir for the App
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    DB_USER = "root"
    DB_PASS = "Tommyjr@1998"

    # Connection to Postgres server
    SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASS + '@34.69.64.239/user'

    # To suppress FSADeprecationWarning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
