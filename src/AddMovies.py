from datetime import datetime
from database import db, Movie

movies_data = [
    {"Title": "Inception", "ReleaseDate": "2010-07-16", "Genre": "Sci-Fi", "Director": "Christopher Nolan", "UrlImage": "https://posters.movieposterdb.com/10_06/2010/1375666/l_1375666_07030c72.jpg"},
    {"Title": "The Shawshank Redemption", "ReleaseDate": "1994-09-23", "Genre": "Drama", "Director": "Frank Darabont", "UrlImage": "https://posters.movieposterdb.com/05_03/1994/0111161/l_8494_0111161_3bb8e662.jpg"},
    {"Title": "The Dark Knight", "ReleaseDate": "2008-07-18", "Genre": "Action", "Director": "Christopher Nolan", "UrlImage": "https://posters.movieposterdb.com/08_05/2008/468569/l_468569_f0e2cd63.jpg"},
    {"Title": "Pulp Fiction", "ReleaseDate": "1994-10-14", "Genre": "Crime", "Director": "Quentin Tarantino", "UrlImage": "https://posters.movieposterdb.com/07_10/1994/110912/l_110912_55345443.jpg"},
    {"Title": "The Godfather", "ReleaseDate": "1972-03-24", "Genre": "Crime", "Director": "Francis Ford Coppola", "UrlImage": "https://posters.movieposterdb.com/22_07/1972/68646/l_68646_8c811dec.jpg"},
    {"Title": "Forrest Gump", "ReleaseDate": "1994-07-06", "Genre": "Drama", "Director": "Robert Zemeckis", "UrlImage": "https://posters.movieposterdb.com/12_04/1994/109830/l_109830_58524cd6.jpg"},
    {"Title": "The Matrix", "ReleaseDate": "1999-03-31", "Genre": "Action", "Director": "Lana Wachowski, Lilly Wachowski", "UrlImage": "https://posters.movieposterdb.com/06_01/1999/0133093/l_77607_0133093_ab8bc972.jpg"},
    {"Title": "Schindler's List", "ReleaseDate": "1993-12-15", "Genre": "Biography", "Director": "Steven Spielberg", "UrlImage": "https://posters.movieposterdb.com/08_02/1993/108052/l_108052_6ad6d11e.jpg"},
]
#Add more movies as needed

# Add instances to the session and commit changes
with db.session.begin(subtransactions=True):
    for movie_data in movies_data:
        movie = Movie(
            Title=movie_data["Title"],
            ReleaseDate=datetime.strptime(movie_data["ReleaseDate"], "%Y-%m-%d").date(),
            Genre=movie_data["Genre"],
            Director=movie_data["Director"],
            UrlImage=movie_data["UrlImage"]
        )
        db.session.add(movie)

db.session.commit()

print("Movies added successfully!")
