from flask import Blueprint, jsonify, request
from . import db, limiter, require_auth, require_admin
from .models import Donation

main = Blueprint('main', __name__)

# /signup and /login removed — Firebase handles authentication

@main.route('/add_donation', methods=['POST'])
@limiter.limit("10 per hour")
@require_auth
def add_donation():
    data = request.get_json()
    donation = Donation(
        name=data['name'],
        phoneNumber=data['phoneNumber'],
        addLine1=data['addLine1'],
        addLine2=data['addLine2'],
        servedFor=data['servedFor'],
        foodType=data['foodType'],
        userEmail=request.user_email,
    )
    db.session.add(donation)
    db.session.commit()
    return 'Done', 201

@main.route('/userDonations')
@require_auth
def userDonations():
    rows = db.session.query(Donation).filter_by(userEmail=request.user_email).all()
    return jsonify({'donations': [_donation_dict(d) for d in rows]})

# ── Admin-only routes ────────────────────────────────────────────────────────

@main.route('/donations')
@require_admin
def donations():
    rows = Donation.query.all()
    return jsonify({'donations': [_donation_dict(d, include_email=True) for d in rows]})

# ── Helpers ──────────────────────────────────────────────────────────────────

def _donation_dict(d, include_email=False):
    out = {
        'name': d.name,
        'phoneNumber': d.phoneNumber,
        'addLine1': d.addLine1,
        'addLine2': d.addLine2,
        'servedFor': d.servedFor,
        'foodType': d.foodType,
        'dateTime': d.dateTime,
    }
    if include_email:
        out['userEmail'] = d.userEmail
    return out
