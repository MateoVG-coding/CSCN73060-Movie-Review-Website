from db.database import db

class User(db.Model):
    __tablename__ = 'Users'

    Username = db.Column(db.String(255), primary_key=True, nullable=False)
    PasswordHash = db.Column(db.String(255), nullable=False)
    RegistrationDate = db.Column(db.DateTime)

class Movie(db.Model):
    __tablename__ = 'Movies'

    MovieID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(255), nullable=False)
    ReleaseDate = db.Column(db.Date)
    Genre = db.Column(db.String(255))
    Director = db.Column(db.String(255))
    UrlImage = db.Column(db.String(255))

class Review(db.Model):
    __tablename__ = 'Reviews'

    ReviewID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    MovieID = db.Column(db.Integer, db.ForeignKey('Movies.MovieID'))
    Username = db.Column(db.String(255), db.ForeignKey('Users.Username'))
    ReviewText = db.Column(db.Text)
    ReviewDate = db.Column(db.DateTime)

class Rating(db.Model):
    __tablename__ = 'Ratings'

    RatingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    MovieID = db.Column(db.Integer, db.ForeignKey('Movies.MovieID'))
    Username = db.Column(db.String(255), db.ForeignKey('Users.Username'))
    RatingValue = db.Column(db.Integer)
    RatingDate = db.Column(db.DateTime)

class Like(db.Model):
    __tablename__ = 'Likes'

    LikeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(255), db.ForeignKey('Users.Username'))
    ReviewID = db.Column(db.Integer, db.ForeignKey('Reviews.ReviewID'))
    LikeDate = db.Column(db.DateTime)

class UserAuthentication(db.Model):
    __tablename__ = 'UserAuthentication'

    AuthID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(255), db.ForeignKey('Users.Username'))
    AttemptTime = db.Column(db.DateTime)
    IPAddress = db.Column(db.String(255))
    AttemptResult = db.Column(db.Boolean)