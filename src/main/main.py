from flask import Flask
from  auth.register_routes import auth_bp


app = Flask(__name__)


app.register_blueprint(auth_bp)

@app.route("/")
def hello_world():
    """Basic main function"""
    return "Hello, World!"


