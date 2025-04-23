# fetch_movie_genres
from models.genres import Genre
from database import Database


def main():

    db = Database()
    print(db.fetch_movies())
    # movies = db.fetch_movie_genres()
    # for movie in movies:
    #     print(type(movie.genre_id))
    # print(movies)


if __name__ == '__main__':
    main()
