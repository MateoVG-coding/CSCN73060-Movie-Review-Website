from flask import Blueprint, request, jsonify, session, render_template, redirect
from models import User, UserAuthentication, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

login_bp = Blueprint('login', __name__)

login_bp.secret_key = '123'

@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    """This function is for the login route"""
    if request.method == 'GET':
        # Should return html or js file for login
        return render_template("login.html")
    elif request.method == 'POST':
        data = request.form
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Missing username or password in JSON'}), 400
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_attempt = UserAuthentication(username=username, attempt_time=datetime.utcnow(), attempt_result=True, ip_address = request.remote_addr)
            db.session.add(login_attempt)
            db.session.commit()
            session['username'] = user.username
            return redirect('/movies')
        else:
            login_attempt = UserAuthentication(username=username, attempt_time=datetime.utcnow(), attempt_result=False, ip_address = request.remote_addr)
            db.session.add(login_attempt)
            db.session.commit()
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Invalid request format'}), 400
    
@login_bp.route('/change-password', methods=['GET', 'PATCH'])
def change_password():
    if request.method == 'GET':
        # Return a response for the GET request (e.g., render a template)
        return render_template('change_password.html')

    if 'username' not in session:
        return jsonify({'error': 'User not logged in'}), 401

    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')

    if not current_password or not new_password:
        return jsonify({'error': 'Missing current or new password'}), 400

    if not check_password_hash(user.password_hash, current_password):
        return jsonify({'error': 'Current password is incorrect'}), 401

    # Hash the new password before updating
    user.password_hash = generate_password_hash(new_password)
    db.session.commit()

    return jsonify({'message': 'Password changed successfully'}), 200