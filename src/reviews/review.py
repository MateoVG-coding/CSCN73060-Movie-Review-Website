import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('MovieReview.sql')
cursor = conn.cursor()

def add_review(user_id, movie_id, review_text):
    # Validate data
    if not user_id or not movie_id or not review_text:
        print("Invalid data. UserID, MovieID, and ReviewText are required.")
        return

    # Add a new review
    review_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO Reviews (MovieID, UserID, ReviewText, ReviewDate)
        VALUES (?, ?, ?, ?)
    """, (movie_id, user_id, review_text, review_date))

    conn.commit()
    print("Review added successfully.")



def update_review(user_id, movie_id, review_text, review_id):
    # Validate data
    if not user_id or not movie_id or not review_text or not review_id:
        print("Invalid data. UserID, MovieID, ReviewText and ReviewID are required.")
        return
    
    try:
        review_id = int(review_id)
    except ValueError:
        print("Invalid Review ID. Please enter a valid integer.")
        return

     # Check if the specified review ID exists in the database
    cursor.execute("""
        SELECT * FROM Reviews
        WHERE ReviewID=? AND UserID=? AND MovieID=?
    """, (review_id, user_id, movie_id))

    existing_review = cursor.fetchone()

    if existing_review:
        # If the review ID exists, update the existing review
        review_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE Reviews
            SET ReviewText=?, ReviewDate=?
            WHERE ReviewID=?
        """, (review_text, review_date, review_id))
        conn.commit()
        print("Review updated successfully.")
    else:
        print("Review with the specified ID not found for the given user and movie.")