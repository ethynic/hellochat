import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    OPEN_AI_KEY = os.environ.get('OPEN_AI_KEY') or '1234567890'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class Dev_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    

class Prod_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    
config = {
    'dev': Dev_config,
    'prod':Prod_config,

    'default': Dev_config
}


    
