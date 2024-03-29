from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import connect_to_db, db, Movie
from login_routes import login_bp
from register_routes import register_bp
from review_route import review_bp
from homepage_route import home_bp
from movies_routes import movies_bp
from AddMovies import initialize_movies

app = Flask(__name__)

app.secret_key = "123"

connect_to_db(app)
with app.app_context():
    db.create_all()

with app.app_context():
    initialize_movies()

# Register blueprints
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(review_bp)
app.register_blueprint(home_bp)
app.register_blueprint(movies_bp)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)