from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel
from enum import auto, StrEnum, Enum
from enum import IntEnum


class MyCounter:
    def __init__(self):
        self._num = -1

    def get(self):
        self._num += 1
        return str(self._num)


num = MyCounter()


class MovieColumn(Enum):
    MOVIE = 0
    GENRE = 1


class Column(StrEnum):
    MOVIE = str(num.get())
    GENRE = str(num.get())

    @staticmethod
    def int_value(col):
        return int(col.value)


class MovieTable:
    MOVIE_TITLE_HEADING, GENRE_HEADING = range(2)

    def create_movie_model(self, parent):
        model = QStandardItemModel(0, 2, parent)
        horizontal = Qt.Orientation.Horizontal
        for column in MovieColumn:
            model.setHeaderData(column.value, horizontal, column.name.title())
        # model.setHeaderData(Column.int_value(Column.GENRE), horizontal, Column.GENRE.name.title())

        return model

    def add_movie(self, model, title: str, genres: str, lst: dict[str, str]):
        for i in lst.values():
            print(i)
        for v
        model.insertRow(0)
        # model.setData(model.index(0, MovieColumn.MOVIE.value), title)
        # model.setData(model.index(0, MovieColumn.GENRE.value), genres)

        # for i in lst.items():
        #     print(i)
        #
        #     for k, v in lst.items():
        #         for column in MovieColumn:
        #             model.setData(model.index(0, column.value), v)ź
            # data = title if column.MOVIE else genres
            # model.setData(model.index(0, column.value), data)
            #


