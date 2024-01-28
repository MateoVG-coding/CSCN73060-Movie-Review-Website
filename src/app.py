from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import connect_to_db, db
from login_routes import login_bp

app = Flask(__name__)

if __name__ == "__main__":
    connect_to_db(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(login_bp)

    app.run(debug=True)