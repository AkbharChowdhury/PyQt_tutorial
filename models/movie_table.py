from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel


class MovieColumn(Enum):
    MOVIE = 0
    GENRE = 1


class MovieTable:

    def create_model(self, parent):
        model = QStandardItemModel(0, 2, parent)
        horizontal = Qt.Orientation.Horizontal
        for column in MovieColumn:
            model.setHeaderData(column.value, horizontal, column.name.title())
        return model

    def add_movie(self, model: QStandardItemModel, data: dict[str, str]):
        model.insertRow(0)
        for key, value in data.items():
            model.setData(model.index(0, MovieColumn[key].value), value)
