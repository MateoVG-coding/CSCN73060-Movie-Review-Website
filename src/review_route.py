from flask import Blueprint, request, jsonify, redirect, render_template, session, url_for
from datetime import datetime
from models import Review, User, Movie, db, Rating

review_bp = Blueprint('review', __name__)

@review_bp.route('/add_review/<int:movie_id>', methods=['GET', 'POST'])
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
        data = request.form
        if 'movie_ID' not in data or 'review_text' not in data or 'rating' not in data:
            return jsonify({'error': 'Missing movie_ID, review_text or rating in JSON'}), 400


        movie_ID = data['movie_ID']  # Adjust the attribute name here
        review_text = data['review_text']
        rating = data['rating']

        if 'username' in session:
            username = session['username']

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

        return redirect('/movies')
    else:
        return jsonify({'error': 'Invalid request format'}), 400

@review_bp.route('/update_review/<int:movie_id>', methods=['PUT', 'GET'])
def update_review(movie_id):
    """This function is for the route to update an existing review"""

    if request.method == 'GET':
        movie = Movie.query.get(movie_id)
        user_id = session['username']
        rating = Rating.query.filter_by(movie_ID=movie_id, username=user_id).first()
        review = Review.query.filter_by(movie_ID=movie_id, username=user_id).first()

        return render_template(
            "update_review.html",
            movie=movie,
            user_ID=user_id,
            rating=rating,
            review=review
        )
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        if 'review_ID' not in data or 'review_text' not in data or 'rating' not in data or 'rating_id' not in data:
            return jsonify({'error': 'Missing username, movie_ID, review_ID, or review_text in JSON'}), 400
        
        review_id = data['review_ID']
        review_text = data['review_text']
        rating_id=data['rating_id']
        rating=data['rating']

        # Validate data and perform review update logic
        review_updated = Review.query.filter_by(review_ID=review_id).first()
        rating_updated = Rating.query.filter_by(rating_ID=rating_id).first()

        if review_updated and rating_updated:

            review_updated.review_text = review_text
            review_updated.review_date = datetime.utcnow()

            rating_updated.rating_value = rating
            rating_updated.rating_date = datetime.utcnow()

            db.session.commit()
            
            return redirect('/movies', code=200)  # ISSUE: Not redirecting to "/movies"
        else:
            return jsonify({'error': 'Failed to update review. Review not found or unauthorized.'}), 400
    else:
        return jsonify({'error': 'Invalid request format'}), 400
    

@review_bp.route('/delete_review/<int:movie_id>', methods=['DELETE', 'GET'])
def delete_review(movie_id):
    """This function is for the route to update an existing review"""
    
    if request.method == 'DELETE':
        movie = Movie.query.get(movie_id)
        user_id = session['username']

        review = Review.query.filter_by(movie_ID=movie_id, username=user_id).first()
        rating = Rating.query.filter_by(movie_ID=movie_id, username=user_id).first()

        if not review and not rating:
            return jsonify({'error': 'Review not found or unauthorized.'}), 400
        
        db.session.delete(review)
        db.session.delete(rating)
        db.session.commit()

        return redirect('/movies')
    else:
        return jsonify({'error': 'Invalid request format'})
        
    