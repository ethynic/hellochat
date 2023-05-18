import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'hell0_flask'
    OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

    @staticmethod
    def init_app(app):
        pass

class Dev_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    
class Prod_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    
class ProdDocker_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Prod_config.init_app(app)

        # 把日志输出到stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    
    
config = {
    'dev': Dev_config,
    'prod':Prod_config,
    'docker':ProdDocker_config,
    'default': Dev_config
}


    
