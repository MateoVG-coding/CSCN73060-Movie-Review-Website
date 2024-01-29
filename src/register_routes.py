from flask import Blueprint, request, jsonify, render_template
from models import User, UserAuthentication, db
from werkzeug.security import generate_password_hash
from datetime import datetime

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST', 'GET'])
def register():
    """This function is for the registration route"""

    if request.method == 'GET':
        # Should return html or js file for register
        return render_template("register.html")
    elif request.method == 'POST':
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Missing username or password in JSON'}), 400

        username = data['username']
        password = data['password']

        # Check if the username already exists in the database
        existing_user = User.query.filter(User.username == username).first()

        if existing_user:
            return jsonify({'error': 'Username already exists. Choose a different one.'}), 400

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='scrypt')

        # Create a new user and add it to the database
        new_user = User(username=username, password_hash=hashed_password, registration_date=datetime.utcnow())
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Registration successful'}), 200
    else:
        return jsonify({'error': 'Invalid request format'}), 400


    
