from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel

from models.my_counter import MyCounter


counter = MyCounter(start_index=-1)

class MovieColumn(Enum):
    MOVIE = counter.get_counter()
    GENRE = counter.get_counter()


class MovieTable:

    def create_model(self, parent):
        model = QStandardItemModel(0, len(MovieColumn), parent)
        horizontal = Qt.Orientation.Horizontal
        for column in MovieColumn:
            model.setHeaderData(column.value, horizontal, column.name.title())
        return model

    @staticmethod
    def add_movie(model: QStandardItemModel, movies: dict[str, str]):
        model.insertRow(0)
        for key, value in movies.items():
            model.setData(model.index(0, MovieColumn[key].value), value)
