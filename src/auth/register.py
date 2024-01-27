import sqlite3
from datetime import datetime


# Connect to the SQLite database
conn = sqlite3.connect('MovieReview.sql')
cursor = conn.cursor()

def create_user(username, password, email):
    # Validate data (add your own validation logic here)
    if not username or not password:
        print("Invalid data. Username and password are required.")
        return

    # Check if the username already exists
    cursor.execute("SELECT * FROM Users WHERE Username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Username already exists. Please choose a different one.")
        return

    # If the username is unique, insert the new user into the Users table
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO Users (Username, Password, Email, RegistrationDate)
        VALUES (?, ?, ?, ?)
    """, (username, password, email, registration_date))

    conn.commit()
    print("User registered successfully.")