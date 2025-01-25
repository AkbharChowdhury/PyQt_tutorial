import psycopg2
from config import load_config
from models.genres import Genre


class Database:
    def fetch_all_genres(self) -> list[Genre]:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT genre_id, genre FROM genres ORDER BY genre")
                return [Genre(row[1], row[0]) for row in cursor.fetchall()]

                # return [Genre(row['genre'], row['genre_id']) for row in cursor.fetchall()]

    def add_movie(self, name):
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO movies(title) VALUES(%s) RETURNING movie_id;', (name,))
                return cur.fetchone()[0]

    def add_movie_genres(self, movie_id: int, genre_id_list: set[int]):
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                for genre_id in genre_id_list:
                    cur.execute("""
                                          INSERT INTO movie_genres (movie_id, genre_id)
                                          VALUES (
                                          %(movie_id)s,
                                           %(genre_id)s
                                          );
                                          """, {
                        'movie_id': movie_id,
                        'genre_id': genre_id,
                    })
