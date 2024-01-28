import sys
sys.path.append('./src')

import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from models import db, connect_to_db, User, UserAuthentication
from login_routes import login_bp
from werkzeug.security import generate_password_hash, check_password_hash

class LoginRouteTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Connect to the in-memory database using connect_to_db
        connect_to_db(self.app)

        # Register the login blueprint
        self.app.register_blueprint(login_bp)

        # Set up a test client
        self.client = self.app.test_client()

        # Create all tables
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop all tables after the test
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_successful(self):
        # Add a test user to the database
        with self.app.app_context():
            test_user = User(username='test_user', password_hash=generate_password_hash('test_password', method='scrypt', salt_length=8))
            db.session.add(test_user)
            db.session.commit()

        # Make a POST request to the login route with correct credentials
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_password'})

        # Check if the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        # Make a POST request to the login route with incorrect credentials
        response = self.client.post('/login', json={'username': 'nonexistent_user', 'password': 'wrong_password'})

        # Check if the response is as expected
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

if __name__ == '__main__':
    unittest.main()