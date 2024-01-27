from flask import Blueprint, jsonify, request

like_bp = Blueprint('like', __name__)

@like_bp.route('/movies/<int:movie_id>/like', methods=['POST'])
def like_movie(movie_id):

    if request.is_json:

        data = request.get_json()
        username = data.get('username')
        review_id = data.get('review_id')

        if not all([username, review_id]):
            return jsonify({'error': 'Missing username or review_id in JSON'}), 400

        #There should be a function to register like in db
        return jsonify({'message': 'Movie liked successfully'}), 200
                       
    else:
        return jsonify({'error': 'Invalid request format'}), 400