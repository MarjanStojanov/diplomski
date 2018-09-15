import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
        Postavljane varijabli unutar aplikacije
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'mit.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Flask je zakon'
