from database import Database


class SearchMovie:
    @staticmethod
    def any_genres():
        return 'Any'
    def __init__(self, title, genre, db: Database):
        self.title: str = title
        self.genre: str = genre
        self.__db: Database = db

    def filter_movie(self):
        return self.__db.fetch_movies(self.title, self.genre)
