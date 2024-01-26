from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

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

        #There should be a function to store the login attempt wether is successfully or not.

        if check_password_hash("mock-data", password):#Should check the hash password from the db
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Invalid request format'}), 400
    