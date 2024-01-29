from flask import Blueprint, request, jsonify, redirect, render_template
from datetime import datetime
from models import Review, User, Movie, db, Rating

review_bp = Blueprint('review', __name__)

@review_bp.route('/add_review/<int:movie_id>', methods=['GET'])
def add_review(movie_id):
    """This function is for the route to add a new review"""

    if request.method == 'GET':
        # Should return html or js file to add review

        movie = Movie.query.get(movie_id)

        return render_template(
            "add_review.html",
            movie=movie,
        )
    elif request.method == 'POST':
        data = request.json
        if 'username' not in data or 'movie_ID' not in data or 'review_text' not in data or 'rating' not in data:
            return jsonify({'error': 'Missing username, movie_ID, or review_text in JSON'}), 400

        username = data['username']
        movie_ID = data['movie_ID']  # Adjust the attribute name here
        review_text = data['review_text']
        rating = data['rating']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()
        movie = Movie.query.filter_by(movie_ID=movie_ID).first()

        if not user:
            return jsonify({'error': 'User not found.'}), 400
        elif not movie:
            return jsonify({'error': 'Movie not found.'}), 400

        # Create a new review and add it to the database
        new_review = Review(movie_ID=movie_ID, username=username, review_text=review_text, review_date=datetime.utcnow())
        new_rating = Rating(movie_ID=movie_ID, username=username, rating_value=rating, rating_date=datetime.utcnow())
        db.session.add(new_review)
        db.session.add(new_rating)
        db.session.commit()

        return redirect('/movies', code=200)
    else:
        return jsonify({'error': 'Invalid request format'}), 400

@review_bp.route('/update_review/<int:movie_id>', methods=['PUT', 'GET'])
def update_review(movie_id):
    """This function is for the route to update an existing review"""

    if request.method == 'GET':
        # Should return html or js file to update review
        return jsonify({'username': 'username', 'password': 'password'})
    elif request.method == 'PUT':
        data = request.json
        if 'username' not in data or 'movie_ID' not in data or 'review_ID' not in data or 'review_text' not in data or 'rating' not in data or 'rating_id' not in data:
            return jsonify({'error': 'Missing username, movie_ID, review_ID, or review_text in JSON'}), 400

        user_id = data['username']
        movie_id = data['movie_ID']
        review_id = data['review_ID']
        review_text = data['review_text']
        rating_id=data['rating_id']
        rating=data['rating']

        # Validate data and perform review update logic
        review_updated = Review.query.filter_by(review_ID=review_id).first()
        rating_updated = Rating.query.filter_by(rating_ID=rating_id).first()

        if review_updated & rating_updated:

            review_updated.ReviewText = review_text
            review_updated.ReviewDate = datetime.utcnow()

            rating_updated.rating_value = rating
            rating_updated.rating_date = datetime.utcnow()

            db.session.commit()
            
            return redirect('/movies', code=200)
        else:
            return jsonify({'error': 'Failed to update review. Review not found or unauthorized.'}), 400
    else:
        return jsonify({'error': 'Invalid request format'}), 400
    

@review_bp.route('/delete_review', methods=['DELETE', 'GET'])
def delete_review():
    """This function is for the route to update an existing review"""
    
    if request.method == 'DELETE':
        data = request.json
        if 'username' not in data or 'review_ID' not in data or 'rating_id' not in data:
            return jsonify({'error': 'Missing username, movie_ID, review_ID, or review_text in JSON'}), 400
        
        user_id = data['username']
        review_id = data['review_ID']
        rating_id = data['rating_id']

        review = Review.query.filter_by(review_ID=review_id, username=user_id).first()
        rating = Rating.query.filter_by(rating_ID=rating_id).first()

        if not review & rating:
            return jsonify({'error': 'Review not found or unauthorized.'}), 400
        
        db.session.delete(review)
        db.session.delete(rating)
        db.commit()

        return redirect('/movies', code=200)
    else:
        return jsonify({'error': 'Invalid request format'})
        
    