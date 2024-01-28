from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'

    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.DateTime)

class Movie(db.Model):
    __tablename__ = 'Movies'

    movie_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    genre = db.Column(db.String(255))
    director = db.Column(db.String(255))
    url_image = db.Column(db.String(255))

class Review(db.Model):
    __tablename__ = 'Reviews'

    review_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_ID = db.Column(db.Integer, db.ForeignKey('Movies.movie_ID'))
    username = db.Column(db.String(255), db.ForeignKey('Users.username'))
    review_text = db.Column(db.Text)
    review_date = db.Column(db.DateTime)

class Rating(db.Model):
    __tablename__ = 'Ratings'

    rating_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_ID = db.Column(db.Integer, db.ForeignKey('Movies.movie_ID'))
    username = db.Column(db.String(255), db.ForeignKey('Users.username'))
    rating_value = db.Column(db.Integer)
    rating_date = db.Column(db.DateTime)

class Like(db.Model):
    __tablename__ = 'Likes'

    like_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), db.ForeignKey('Users.username'))
    review_ID = db.Column(db.Integer, db.ForeignKey('Reviews.review_ID'))
    like_date = db.Column(db.DateTime)

class UserAuthentication(db.Model):
    __tablename__ = 'UserAuthentication'

    auth_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), db.ForeignKey('Users.username'))
    attempt_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_adddress = db.Column(db.String(255))
    attempt_result = db.Column(db.Boolean)

def connect_to_db(app):
    sqlite_uri = 'sqlite:///' + 'C:/Users/Mateo V.G/source/repos/CSCN73060-ProjectVI-MovieReview-Website/src/database_movies.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
