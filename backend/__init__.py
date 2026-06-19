import os
from functools import wraps
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per hour", "60 per minute"])

# ── Firebase Admin SDK ──────────────────────────────────────────────────────
_sa_path = os.getenv('FIREBASE_SERVICE_ACCOUNT_PATH', 'service-account.json')
try:
    firebase_admin.initialize_app(credentials.Certificate(_sa_path))
except Exception as _e:
    print(f"[warn] Firebase Admin not initialised ({_e}). Auth routes will return 503.")

def _verify_token():
    token = request.headers.get('Authorization', '').removeprefix('Bearer ').strip()
    if not token:
        return None, ('Missing token', 401)
    try:
        decoded = firebase_auth.verify_id_token(token)
        return decoded, None
    except Exception:
        return None, ('Invalid or expired token', 401)

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not firebase_admin._apps:
            return 'Auth service unavailable', 503
        decoded, err = _verify_token()
        if err:
            return err
        request.user_email = decoded.get('email', '')
        request.user_uid = decoded.get('uid', '')
        return f(*args, **kwargs)
    return decorated

def require_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not firebase_admin._apps:
            return 'Auth service unavailable', 503
        decoded, err = _verify_token()
        if err:
            return err
        admin_email = os.getenv('ADMIN_EMAIL', '')
        if not admin_email or decoded.get('email') != admin_email:
            return 'Forbidden', 403
        request.user_email = decoded.get('email', '')
        request.user_uid = decoded.get('uid', '')
        return f(*args, **kwargs)
    return decorated

# ── App factory ─────────────────────────────────────────────────────────────
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    limiter.init_app(app)
    from .services import main
    app.register_blueprint(main)
    return app
