from typing import Any

import psycopg2
from config import load_config
from models.genres import Genre
import psycopg2.extras


class Database:

    def fetch_movie_genres(self) -> list[Genre]:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("SELECT genre, genre_id FROM available_movie_genres")
                return [Genre(name=row['genre'], genre_id=row['genre_id']) for row in cursor.fetchall()]

    def fetch_all_genres(self) -> list[Genre]:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("SELECT genre_id, genre FROM genres ORDER BY genre")
                return [Genre(name=row['genre'], genre_id=row['genre_id']) for row in cursor.fetchall()]

    def fetch_movies(self, title: str = '', genre: str = '') -> list[dict[str, Any]]:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(f"SELECT movie_id, title, genres FROM fn_get_movies('%{title}%','%{genre}%')")
                data = [dict(row) for row in cursor.fetchall()]
                return sorted(data, key=lambda d: d.get('title'))
                # return sorted(data[0], key=lambda x:x['title'])
                # return [dict(row) for row in cursor.fetchall()]

    def add_movie(self, name):
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO movies(title) VALUES(%s) RETURNING movie_id;', ([name]))
                return cursor.fetchone()[0]

    def update_movie(self, movie_id: int, title: str):
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                                        UPDATE movies 
                                        SET title = %(title)s
                                        WHERE movie_id = %(movie_id)s
                                                                """, {
                    'title': title,
                    'movie_id': movie_id,
                })

    def delete(self, id_field: str, table: str, num: int):
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f'DELETE FROM {table} WHERE {id_field} = %s;', ([num]))

    def add_movie_genres(self, movie_id: int, genre_id_list: set[int]):
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for genre_id in genre_id_list:
                    cur.execute("""
                                              INSERT INTO movie_genres (movie_id, genre_id) VALUES (
                                              %(movie_id)s,
                                               %(genre_id)s
                                              );
                                              """, {
                        'movie_id': movie_id,
                        'genre_id': genre_id,
                    })
