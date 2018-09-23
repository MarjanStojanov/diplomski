import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
        Postavljane varijabli unutar aplikacije
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'mit.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Flask je zakon'
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'marjanstojanov996@gmail.com',
    MAIL_PASSWORD = 'mari0nmari0n',
    MAIL_SUPPRESS_SEND = False,
    MAIL_DEBUG = True
