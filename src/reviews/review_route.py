from flask import Blueprint, request, jsonify
from datetime import datetime

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/add_review', methods=['POST'])
def add_review():
    """This function is for the route to add a new review"""
    if request.is_json:
        data = request.json
        if 'user_id' not in data or 'movie_id' not in data or 'review_text' not in data:
            return jsonify({'error': 'Missing user_id, movie_id, or review_text in JSON'}), 400

        user_id = data['user_id']
        movie_id = data['movie_id']
        review_text = data['review_text']

        # Validate data and perform review addition logic
        review_added = add_review(user_id, movie_id, review_text)

        if review_added:
            return jsonify({'message': 'Review added successfully'})
        else:
            return jsonify({'error': 'Failed to add review. User or movie not found.'}), 400
    else:
        return jsonify({'error': 'Invalid request format'}), 400

@movie_bp.route('/update_review', methods=['PUT'])
def update_review():
    """This function is for the route to update an existing review"""
    if request.is_json:
        data = request.json
        if 'user_id' not in data or 'movie_id' not in data or 'review_id' not in data or 'review_text' not in data:
            return jsonify({'error': 'Missing user_id, movie_id, review_id, or review_text in JSON'}), 400

        user_id = data['user_id']
        movie_id = data['movie_id']
        review_id = data['review_id']
        review_text = data['review_text']

        # Validate data and perform review update logic
        review_updated = update_review(user_id, movie_id, review_text, review_id)

        if review_updated:
            return jsonify({'message': 'Review updated successfully'})
        else:
            return jsonify({'error': 'Failed to update review. Review not found or unauthorized.'}), 400
    else:
        return jsonify({'error': 'Invalid request format'}), 400