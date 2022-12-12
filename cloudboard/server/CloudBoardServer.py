from flask import Blueprint, render_template, flash, request, Response
from flask_login import login_required, current_user
from .models import User, Device, Clipboard
from sqlalchemy import select
import jsonpickle
import jwt
import hashlib
from datetime import datetime
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    name = current_user.name
    current_devices = current_user.devices
    devices = {}
    for device in current_devices:
        devices[device.name] = {"id": device.id, "token": device.token_hash}
    return render_template("profile.html", name=name, devices=devices)


@main.route("/delete_device", methods=["POST"])
def delete_device():
    device_id = request.form.get("delete")
    if device_id:
        Device.query.filter_by(id=device_id).delete()
        db.session.commit()
    name = current_user.name
    current_devices = current_user.devices
    devices = {}
    for device in current_devices:
        devices[device.name] = {"id": device.id, "token": device.token_hash}
    return render_template("profile.html", name=name, devices=devices)


@main.route("/add_device", methods=["POST"])
@login_required
def add_device():
    device_name = request.form.get("device")
    if device_name:

        jwt_token = jwt.encode({"name": device_name}, "secret", algorithm="HS256")
        encoded_jwt = hashlib.sha256(jwt_token.encode("utf-8")).hexdigest()
        device = Device(
            name=device_name, token_hash=encoded_jwt, user_id=current_user.id
        )
        db.session.add(device)
        db.session.commit()
        flash(
            f"Device {device_name} added. Please copy the token {jwt_token} and store it in a safe place."
        )
    name = current_user.name
    current_devices = current_user.devices
    devices = {}
    for device in current_devices:
        devices[device.name] = {"id": device.id, "token": device.token_hash}
    return render_template("profile.html", name=name, devices=devices)


@main.route("/copy_data", methods=["POST"])
def copy_data():
    r = request
    try:
        json_data = jsonpickle.decode(r.data)
        print(f"Decoded json is {json_data}")
        jwt_token = json_data["device_id"]
        copy_data = json_data["copy_data"]
        timestamp = datetime.strptime(json_data["timestamp"], "%m/%d/%y %H:%M:%S")
        is_file = json_data["is_file"]
        encoded_jwt = hashlib.sha256(jwt_token.encode("utf-8")).hexdigest()
        device = Device.query.filter_by(token_hash=encoded_jwt).first()

        if device:
            clipboard = Clipboard(
                copied_at=timestamp,
                copied_data=copy_data,
                is_file=is_file,
                device_id=device.id,
            )
            db.session.add(clipboard)
            db.session.commit()
            response = {"message": "copied successfully", "error": False}
        else:
            response = {"message": "device not found", "error": True}

    except Exception as e:
        print(e)
        response = {"message": "Unexpected error", "error": True}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


@main.route("/list_clipboards", methods=["GET"])
def list_clipboards():
    r = request
    
    json_data = jsonpickle.decode(r.data)
    jwt_token = json_data["device_id"]
    encoded_jwt = hashlib.sha256(jwt_token.encode("utf-8")).hexdigest()
    device = Device.query.filter_by(token_hash=encoded_jwt).first()
    if device:
        clipboards = Clipboard.query.filter_by(device_id=device.id).order_by(Clipboard.copied_at.desc()).all()
        # convert clipboards to dict
        clipboards_list = []
        for clipboard in clipboards:
            clipboards_list.append({
                "id": clipboard.id,
                "copied_at": clipboard.copied_at.strftime("%m/%d/%y %H:%M:%S"),
                "copied_data": clipboard.copied_data,
                "is_file": clipboard.is_file,
            })
        clipboards_hash = {"clipboards": clipboards_list}
        clipboards_pickled = jsonpickle.encode(clipboards_hash)
        return Response(
            response=clipboards_pickled, status=200, mimetype="application/json"
        )
    else:
        return Response(
            response="device not found", status=404, mimetype="application/json"
        )
