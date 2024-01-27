from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from db.models import User, UserAuthentication
from db import db
import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """This function is for the login route"""
    if request.is_json:
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Missing username or password in JSON'}), 400
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # Log successful login attempt
            login_attempt = UserAuthentication(Username=username, AttemptTime=datetime.utcnow(), AttemptResult=True)
            db.session.add(login_attempt)
            db.session.commit()
            return jsonify({'message': 'Login successful'})
        else:
            login_attempt = UserAuthentication(Username=username, AttemptTime=datetime.utcnow(), AttemptResult=False)
            db.session.add(login_attempt)
            db.session.commit()
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Invalid request format'}), 400
    