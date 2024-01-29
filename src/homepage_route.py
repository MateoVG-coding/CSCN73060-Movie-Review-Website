from flask import Blueprint, request, jsonify, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    """Homepage."""
    
    # Should return html or js file for the homepage
    return render_template("homepage.html")