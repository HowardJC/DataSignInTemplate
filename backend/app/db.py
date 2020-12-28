from app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"

db=SQLAlchemy(app)



class Users(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True) # primary_key makes it so that this value is unique and can be used to identify this record.
    username = db.Column(db.String(24))
    email = db.Column(db.String(64))
    pwd = db.Column(db.String(64))

    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

db.create_all()
