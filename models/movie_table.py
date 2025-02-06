from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel

from models.my_counter import MyCounter

counter = MyCounter(start_index=-1)


class MovieColumn(Enum):
    TITLE = counter.get_counter()
    GENRES = counter.get_counter()
    MOVIE_ID = counter.get_counter()


del counter


class MovieTable:

    def create_model(self, parent):
        model = QStandardItemModel(0, len(MovieColumn), parent)
        horizontal = Qt.Orientation.Horizontal
        for column in MovieColumn:
            model.setHeaderData(column.value, horizontal, column.name.title())
        return model

    @staticmethod
    def add_movies(model: QStandardItemModel, movies: list[dict[str, str]]):
        del movies[0][MovieColumn.MOVIE_ID.name]
        movies.reverse()
        for movie in movies:
            model.insertRow(0)
            for key, value in movie.items():
                model.setData(model.index(0, MovieColumn[key].value), value)
