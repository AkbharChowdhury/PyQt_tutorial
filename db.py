import psycopg2
from config import load_config
from genres import Genre


class Database:
    def fetch_all_genres(self) -> list[Genre]:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM genres ORDER BY genre")
                # for row in cursor.fetchall():
                #     print(type(row))

                return [Genre(row[0], row[1]) for row in cursor.fetchall()]
