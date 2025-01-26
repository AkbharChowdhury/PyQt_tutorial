from db import Database
db = Database()
movies = db.fetch_movies()
print(movies)
data: dict[str, str] = list(filter(lambda x: x['movie_id'] == 40, movies))[0]
print(data)
genres = data.get('genres')
print(genres.split(' | '))
# print(db.fetch_movie_title(27))
# print(db.delete('movie_id','movies',47))