from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    #posts = db.relationship('Post', backref='user', passive_deletes=True)
class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    soilmoisture = db.Column(db.String(150))
    temperature = db.Column(db.String(150))
    humidity = db.Column(db.String(10))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

#class Post(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #int_data = db.Column(db.Integer, nullable=False)
    #date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    #author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)