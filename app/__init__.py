from flask import Flask,request,redirect,render_template,url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

db = SQLAlchemy()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    CORS.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.route('/')
    def index():
        return redirect(url_for(main.index))

    app.app_context()
    return app
