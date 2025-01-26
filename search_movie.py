from db import Database


class SearchMovie:
    def __init__(self, title, genre, db: Database):
        self.title: str = title
        self.genre: str = genre
        self.db: Database = db

    def filter_movie(self):
        return self.db.fetch_movies(self.title, self.genre)
