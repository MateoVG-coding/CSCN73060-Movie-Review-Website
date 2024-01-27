from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from auth.register import create_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    """This function is for the registration route"""

    if request.method == 'GET':
        #used to test if web client receiving get requests from server 
        return jsonify({'username': 'username', 'password': 'password', 'email': 'email'})
    elif request.method == 'POST':
        if request.is_json:
            data = request.json
            if 'username' not in data or 'password' not in data or 'email' not in data:
                return jsonify({'error': 'Missing username, password, or email in JSON'}), 400

            username = data['username']
            password = data['password']
            email = data['email']

            # Validate data and perform registration logic
            registration_successful = create_user(username, password, email)

            if registration_successful:
                return jsonify({'message': 'Registration successful'})
            else:
                return jsonify({'error': 'Registration failed. Username or email may already be taken.'}), 400
        else:
            return jsonify({'error': 'Invalid request format'}), 400
        


    
