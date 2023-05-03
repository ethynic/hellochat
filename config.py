import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'hell0_flask'

    @staticmethod
    def init_app(app):
        pass

class Dev_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    OPEN_AI_KEY = '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'
    

class Prod_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    OPEN_AI_KEY = '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'
    
config = {
    'dev': Dev_config,
    'prod':Prod_config,
    'default': Dev_config
}


    
