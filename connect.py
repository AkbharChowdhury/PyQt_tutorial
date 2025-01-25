import psycopg2
from config import load_config


class Database:
    def __init__(self):
        self.__config =  load_config()

    def fetch_all_genres(self):
        with psycopg2.connect(**self.__config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM genres ORDER BY genre")
                return cursor.fetchall()


if __name__ == '__main__':
    db = Database()
    print(db.fetch_all_genres())
