from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # devices = db.relationship("Device", backref="post")
    # clipboards = db.relationship("Clipboard", backref="post")
    devices = db.relationship("Device", back_populates = "user")
    clipboards = db.relationship("Clipboard", back_populates = "user")


class Device(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    token_hash = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    user = db.relationship("User", back_populates = "devices")
    clipboards = db.relationship("Clipboard", back_populates ="device")

class Clipboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    copied_at = db.Column(db.DateTime)
    copied_data = db.Column(db.String(100000))
    is_file = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))
    device = db.relationship("Device", back_populates = "clipboards" )
    user = db.relationship("User", back_populates = "clipboards")
