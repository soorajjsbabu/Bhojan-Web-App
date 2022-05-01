from flask import Blueprint, jsonify, request
from . import db 
from .models import User, Donation
from sqlalchemy import update

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()

    new_user = User(phoneNumber=user_data['phoneNumber'], name=user_data['name'], email=user_data['email'])

    db.session.add(new_user)
    db.session.commit()

    return 'Done', 201

@main.route('/update_user', methods=['PUT'])
def update_user():
    user_data = request.get_json()
    print(user_data)
    db.session.query(User).\
       filter(User.phoneNumber == user_data['phoneNumber']).\
       update({"name":user_data['name'], "email":user_data['email']})
    db.session.commit()

    return 'Done', 201

@main.route('/delete_user/<phoneNumber>', methods=['DELETE'])
def delete_user(phoneNumber):
    db.session.query(User).\
       filter(User.phoneNumber == phoneNumber).delete()
    db.session.commit()

    return 'Done', 201

@main.route('/users')
def users():
    user_details = User.query.all()
    users = []

    for user in user_details:
        users.append({'phoneNumber' : user.phoneNumber, 'name' : user.name, 'email' : user.email})

    return jsonify({'users' : users})

@main.route('/add_donation', methods=['POST'])
def add_donation():
    donation_data = request.get_json()

    new_donation = Donation(name=donation_data['name'], phoneNumber=donation_data['phoneNumber'], addLine1=donation_data['addLine1'], addLine2=donation_data['addLine2'], servedFor=donation_data['servedFor'], foodType=donation_data['foodType'])

    db.session.add(new_donation)
    db.session.commit()

    return 'Done', 201

@main.route('/donations')
def donations():
    donation_details = Donation.query.all()
    donations = []

    for donation in donation_details:
        donations.append({'name' : donation.name, 'phoneNumber' : donation.phoneNumber, 'addLine1' : donation.addLine1, 'addLine2' : donation.addLine2, 'servedFor' : donation.servedFor, 'foodType': donation.foodType, "dateTime": donation.dateTime})

    return jsonify({'donations' : donations})