from database import Database


def main():
    db = Database()
    genres = db.fetch_all_genres()
    print(genres)


if __name__ == '__main__':
    main()
