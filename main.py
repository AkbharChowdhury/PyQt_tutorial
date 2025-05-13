from database import Database


def main():
    db = Database()
    print(db.fetch_movie_genres())


if __name__ == '__main__':
    main()
