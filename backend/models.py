from . import db 
import datetime

class User(db.Model):
    phoneNumber = db.Column(db.String(10), primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    phoneNumber = db.Column(db.String(10))
    addLine1 = db.Column(db.String(50))
    addLine2 = db.Column(db.String(50))
    servedFor = db.Column(db.Integer)  
    foodType = db.Column(db.String(10))  
    dateTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    userPhone = db.Column(db.String(10), db.ForeignKey('registry.phoneNumber'))

class Registry(db.Model):
    phoneNumber = db.Column(db.String(10), primary_key=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    donations = db.relationship('Donation', backref='registry')
