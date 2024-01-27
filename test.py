from database import db


class User(db.Model):
    __tablename__ = 'Users'

    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255))
    RegistrationDate = db.Column(db.DateTime)


class UserRole(db.Model):
    __tablename__ = 'UserRoles'

    RoleID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RoleName = db.Column(db.String(255), nullable=False)



class UserRoleAssignment(db.Model):
    __tablename__ = 'UserRoleAssignments'

    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key=True)
    RoleID = db.Column(db.Integer, db.ForeignKey('UserRoles.RoleID'), primary_key=True)


class Movie(db.Model):
    __tablename__ = 'Movies'

    MovieID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(255), nullable=False)
    ReleaseDate = db.Column(db.Date)
    Genre = db.Column(db.String(255))
    Director = db.Column(db.String(255))



class Review(db.Model):
    __tablename__ = 'Reviews'

    ReviewID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    MovieID = db.Column(db.Integer, db.ForeignKey('Movies.MovieID'))
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    ReviewText = db.Column(db.Text)
    ReviewDate = db.Column(db.DateTime)


class Rating(db.Model):
    __tablename__ = 'Ratings'

    RatingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    MovieID = db.Column(db.Integer, db.ForeignKey('Movies.MovieID'))
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    RatingValue = db.Column(db.Integer)
    RatingDate = db.Column(db.DateTime)


class Like(db.Model):
    __tablename__ = 'Likes'

    LikeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    ReviewID = db.Column(db.Integer, db.ForeignKey('Reviews.ReviewID'))
    LikeDate = db.Column(db.DateTime)


class UserCredential(db.Model):
    __tablename__ = 'UserCredentials'

    CredentialID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    CredentialHash = db.Column(db.String(255), nullable=False)
    LastUpdated = db.Column(db.DateTime)


class UserAuthentication(db.Model):
    __tablename__ = 'UserAuthentication'

    AuthID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    AttemptTime = db.Column(db.DateTime)
    IPAddress = db.Column(db.String(255))
    AttemptResult = db.Column(db.Boolean)


class LogInError(db.Model):
    __tablename__ = 'LogInErrors'

    ErrorID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    ErrorTime = db.Column(db.DateTime)
    ErrorMessage = db.Column(db.Text)