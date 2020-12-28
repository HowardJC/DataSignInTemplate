from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
from app.db import db
from app.routed import api
from app.routed import Misc
