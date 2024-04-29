from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(datetime.now), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Drone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    status = db.Column(db.String(150))

class Drone_Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    action = db.Column(db.String(150))
    drone = db.Column(db.String(150))
    date = db.Column(db.DateTime(datetime.now), default=func.now())
    note = db.Column(db.String(500))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    notes = db.relationship('Note')
