from . import db
import datetime

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    phoneNumber = db.Column(db.String(20))
    addLine1 = db.Column(db.String(100))
    addLine2 = db.Column(db.String(100))
    servedFor = db.Column(db.Integer)
    foodType = db.Column(db.String(10))
    dateTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    userEmail = db.Column(db.String(100))
