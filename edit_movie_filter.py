from database import Database
from models.genres import Genre
import operator
db = Database()
movies = db.fetch_movies()
print(f'{movies=}')
movie_id: int = 45
data: dict[str, str] = list(filter(lambda x: operator.eq(movie_id, x['movie_id'] ), movies))[0]
print(f'{data=}')
genres: list[str] = data.get('genres').split(Genre.genre_split())
title: str = data.get('title')
print(f'{genres=}')
print(f'{title=}')