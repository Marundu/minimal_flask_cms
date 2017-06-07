import os
class Configuration(object):
    DEBUG=True
    APPLICATION_DIR=os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///{}.db'.format(APPLICATION_DIR)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.urandom(40)
