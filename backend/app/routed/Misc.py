from app import app
from flask import request,jsonify
from app.db import Users
from app.db import db
@app.route('/')
def index():
    return "Hello, world"
