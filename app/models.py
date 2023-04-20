
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy(current_app)

class User(UserMixin, db.model):
    __tablename__ = 't_login'
    id = db.Column(db.Integer, Primary_key=True)
    username = db.Column(db.String(64))
    role_id = db.Column(db.Integer,db.ForiegnKey('t_role.id'))

    def __repr__(self):
        return '<User %r>' % self.username
    
class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name