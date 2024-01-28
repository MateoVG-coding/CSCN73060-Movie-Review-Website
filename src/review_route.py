from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Review, User, Movie, db

review_bp = Blueprint('review', __name__)

@review_bp.route('/add_review', methods=['POST'])
def add_review():
    """This function is for the route to add a new review"""
    if request.is_json:
        data = request.json
        if 'username' not in data or 'movie_ID' not in data or 'review_text' not in data:
            return jsonify({'error': 'Missing username, movie_ID, or review_text in JSON'}), 400

        username = data['username']
        movie_ID = data['movie_ID']  # Adjust the attribute name here
        review_text = data['review_text']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()
        movie = Movie.query.filter_by(movie_ID=movie_ID).first()

        if not user:
            return jsonify({'error': 'User not found.'}), 400
        elif not movie:
            return jsonify({'error': 'Movie not found.'}), 400

        # Create a new review and add it to the database
        new_review = Review(movie_ID=movie_ID, username=username, review_text=review_text, review_date=datetime.utcnow())
        db.session.add(new_review)
        db.session.commit()

        return jsonify({'message': 'Review added successfully'})
    else:
        return jsonify({'error': 'Invalid request format'}), 400

@review_bp.route('/update_review', methods=['PUT'])
def update_review():
    """This function is for the route to update an existing review"""
    if request.is_json:
        data = request.json
        if 'username' not in data or 'movie_ID' not in data or 'review_ID' not in data or 'review_text' not in data:
            return jsonify({'error': 'Missing username, movie_ID, review_ID, or review_text in JSON'}), 400

        user_id = data['username']
        movie_id = data['movie_ID']
        review_id = data['review_ID']
        review_text = data['review_text']

        # Validate data and perform review update logic
        review_updated = Review.query.filter_by(review_ID=review_id).first()

        if review_updated:

            review_updated.ReviewText = review_text
            review_updated.ReviewDate = datetime.utcnow()
            db.session.commit()
            
            return jsonify({'message': 'Review updated successfully'})
        else:
            return jsonify({'error': 'Failed to update review. Review not found or unauthorized.'}), 400
    else:
        return jsonify({'error': 'Invalid request format'}), 400