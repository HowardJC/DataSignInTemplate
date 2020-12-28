from app import app
from flask import request,jsonify
from app.db import Users
from app.db import db
import re

def getUsers():
    users = Users.query.all()
    return [{"id": i.id, "username": i.username, "email": i.email, "password": i.pwd} for i in users]

def addUser(username, email, pwd):
    if (username and pwd and email):
        try:
            user = Users(username, email, pwd)
            db.session.add(user)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False

def removeUser(uid):
    uid = request.json["id"]
    if (uid):
        try:
            user = Users.query.get(uid)
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False


@app.route("/api/login", methods=["POST"])
def login():
    try:
        email = request.json["email"].lower()
        password = request.json["pwd"]
        if (email and password):
            users = getUsers()
            # Check if user exists
            return jsonify(len(list(filter(lambda x: x["email"] == email and x["password"] == password, users))) == 1)
        else:
            return jsonify({"error": "Invalid form"})
    except:
        return jsonify({"error": "Invalid form"})

@app.route("/api/register", methods=["POST"])
def register():
    try:
        email = request.json["email"]
        email = email.lower()
        password = request.json["pwd"]
        username = request.json["username"].lower()
        # Check to see if user already exists
        users = getUsers()
        if(len(list(filter(lambda x: x["email"] == email, users))) == 1):
            return jsonify({"error": "Invalid form since user exists"})
        # Email validation check
        if not re.match(r"[\w\._]{5,}@\w{3,}.\w{2,4}", email):
            return jsonify({"error": "Invalid form"})
        addUser(username, email, password)
        return jsonify({"success": True})
    except:
        return jsonify({"error": "Invalid form"})