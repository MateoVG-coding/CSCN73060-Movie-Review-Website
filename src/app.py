from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import connect_to_db, db
from login_routes import login_bp
from register_routes import register_bp
from review_route import review_bp
from homepage_route import home_bp
from movies_routes import movies_bp

app = Flask(__name__)

if __name__ == "__main__":
    connect_to_db(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(movies_bp)

    app.run(debug=True)