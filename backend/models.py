from . import db 
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(10))
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    phoneNumber = db.Column(db.String(10))
    addLine1 = db.Column(db.String(50))
    addLine2 = db.Column(db.String(50))
    servedFor = db.Column(db.Integer)  
    foodType = db.Column(db.String(10))  
    dateTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(10))
    password = db.Column(db.String(30))
