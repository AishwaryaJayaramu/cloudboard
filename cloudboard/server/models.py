from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    devices = db.relationship("Device", backref="post")
    # clipboards = db.relationship("Clipboard", backref="post")


class Device(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    token_hash = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    clipboards = db.relationship("Clipboard", backref="post")

class Clipboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    copiedAt = db.Column(db.DateTime)
    copiedData = db.Column(db.String(100000))
    isFile = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))
