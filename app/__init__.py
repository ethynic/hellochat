from flask import Flask,request,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
moment = Moment()
bsp = Bootstrap()
lg = LoginManager()
lg.login_view = 'login.login_in'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    

    config[config_name].init_app(app)
    moment.init_app(app)
    db.init_app(app)
    bsp.init_app(app)
    lg.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    @app.route('/')
    def index():
        return redirect(url_for(login.login_in))

    return app
