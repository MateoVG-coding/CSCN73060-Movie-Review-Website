from flask import Blueprint, request, jsonify

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """This function send all the information movie"""

    #This function should send the HTML of the movie from the db
    return 