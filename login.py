import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqllite:///' + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship()

    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(db.Model):
    __tablename__ = 't_login'
    id = db.Column(db.Integer, Primary_key=True)
    username = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username