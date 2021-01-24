import os

#En este archivo se define la configuracion de la app
class Config(object):
    SECRET_KEY = 'my_secret_key'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pitsaluma.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False