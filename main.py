# fetch_movie_genres
from models.genres import Genre
from database import Database


def main():

    db = Database()
    genres = db.fetch_all_genres()
    print(genres)
    # print(sorted(genres, key=lambda x: x['name']))


    # movies = db.fetch_movie_genres()
    # for movie in movies:
    #     print(type(movie.genre_id))
    # print(movies)


if __name__ == '__main__':
    main()
