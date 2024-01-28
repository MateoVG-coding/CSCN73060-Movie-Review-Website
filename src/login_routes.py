from flask import Blueprint, request, jsonify
from models import User, UserAuthentication, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    """This function is for the login route"""
    if request.is_json:
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Missing username or password in JSON'}), 400
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_attempt = UserAuthentication(username=username, attempt_time=datetime.utcnow(), attempt_result=True, ip_address = request.remote_addr)
            db.session.add(login_attempt)
            db.session.commit()
            return jsonify({'message': 'Login successful'}), 200
        else:
            login_attempt = UserAuthentication(username=username, attempt_time=datetime.utcnow(), attempt_result=False, ip_address = request.remote_addr)
            db.session.add(login_attempt)
            db.session.commit()
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Invalid request format'}), 400
    