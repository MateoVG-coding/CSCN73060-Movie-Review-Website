from flask import Blueprint, request, jsonify, render_template, session
from models import Movie, User, Rating, Review

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """This function send all the information movie"""

    #This function should send the HTML of the movie from the db
    movie = Movie.query.get(movie_id)
    user_id = session.get("user_id")
    
    if user_id:
        user_rating = Rating.query.filter_by(movie_ID=movie_id, username=user_id).first()
        review = Review.query.filter_by(movie_ID=movie_id, username=user_id).first()
    else:
        user_rating=None
        review=None
    
    return render_template(
        "movie_page.html",
        movie=movie,
        user_rating=user_rating,
        review=review
    )


@movies_bp.route('/movies', methods=['GET'])
def get_list():
    """This function send all movies"""

    movies=Movie.query.order_by('title').all()

    return render_template("movie_list.html", movies=movies)