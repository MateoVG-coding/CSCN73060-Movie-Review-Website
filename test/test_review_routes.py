import sys
sys.path.append('./src')

import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from models import User, Movie, Review, db, connect_to_db
from review_route import review_bp
from werkzeug.security import generate_password_hash, check_password_hash
import json
from datetime import datetime, date

class ReviewRouteTests(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Connect to the in-memory database using connect_to_db
        connect_to_db(self.app)

        # Register the review blueprint
        self.app.register_blueprint(review_bp)

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

    def test_add_review_success(self):
        # Test code for successfully adding a review
        user = User(username='test_user', password_hash='some_hash', registration_date=datetime.now())
        movie = Movie(title='Test Movie', release_date=date.today(), genre='Action', director='Some Director', url_image='some_url')

        with self.app.app_context():
            db.session.add(user)
            db.session.add(movie)
            db.session.commit()

            # Refresh the objects to make sure they are in sync with the database
            db.session.refresh(user)
            db.session.refresh(movie)

        response = self.client.post('/add_review', json={'username': 'test_user', 'movie_ID': movie.movie_ID, 'review_text': 'Great movie!'})
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Review added successfully')

    def test_add_review_missing_data(self):
        # Test code for missing data in the request for adding a review
        response = self.client.post('/add_review', json={'username': 'test_user', 'review_text': 'Great movie!'})
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Missing username, movie_ID, or review_text in JSON')

    def test_update_review_success(self):
        # Test code for successfully updating a review
        user = User(username='test_user', password_hash='some_hash', registration_date=datetime.now())
        movie = Movie(title='Test Movie', release_date=date.today(), genre='Action', director='Some Director', url_image='some_url')
        review = Review(movie_ID=movie.movie_ID, username=user.username, review_text='Old review text', review_date=datetime.now())

        with self.app.app_context():
            db.session.add(user)
            db.session.add(movie)
            db.session.add(review)
            db.session.commit()

            # Refresh the objects to make sure they are in sync with the database
            db.session.refresh(user)
            db.session.refresh(movie)
            db.session.refresh(review)

        response = self.client.put('/update_review', json={'username': user.username, 'movie_ID': movie.movie_ID, 'review_ID': review.review_ID, 'review_text': 'Updated review text'})
        data = json.loads(response.data.decode('utf-8'))

        print("Response status code:", response.status_code)
        print("Response data:", data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Review updated successfully')

    def test_update_review_missing_data(self):
        # Test code for missing data in the request for updating a review
        response = self.client.put('/update_review', json={'user_id': 'test_user', 'review_id': 1, 'review_text': 'Updated review text'})
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Missing username, movie_ID, review_ID, or review_text in JSON')

if __name__ == '__main__':
    unittest.main()