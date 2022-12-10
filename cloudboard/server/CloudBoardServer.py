from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from .models import Device
import jwt
import hashlib
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template(
        "profile.html",
        name=current_user.name,
        current_devices=list(map(lambda x: x.name, current_user.devices)),
    )


@main.route("/add_device", methods=["POST"])
@login_required
def add_device():
    device_name = request.form.get("device")
    if device_name:
        
        jwt_token = jwt.encode({"name": device_name}, "secret", algorithm="HS256")
        encoded_jwt = hashlib.sha256(jwt_token.encode('utf-8')).hexdigest()
        device = Device(name=device_name, token_hash = encoded_jwt, user_id=current_user.id)
        db.session.add(device)
        db.session.commit()
        flash(f"Device {device_name} added. Please copy the token {jwt_token} and store it in a safe place.")

    return render_template(
        "profile.html", 
        name=current_user.name
    )
