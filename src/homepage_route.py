from flask import (Flask, jsonify, render_template, redirect, request, flash, session)

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage."""
    
    # Should return html or js file for the homepage
    return 