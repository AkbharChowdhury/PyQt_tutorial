import sys
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QIcon

# from PyQt6.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt, QTime)
from PyQt6.QtCore import (QDate, QDateTime, QSortFilterProxyModel, Qt, QTime)

from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QTreeView, QVBoxLayout, QWidget)


class App(QWidget):
    MOVIE_TITLE_HEADING, GENRE_HEADING, DATE = range(3)

    def __init__(self):
        super().__init__()
        self.title = 'movie search'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.dataGroupBox = QGroupBox("Movies")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)

        model = self.createMailModel(self)
        self.dataView.setModel(model)
        from db import Database
        db = Database()
        for i in db.fetch_movies('', ''):
            self.add_movie(model, i.get('title'), i.get('genres'))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)

        self.show()

    def createMailModel(self, parent):
        model = QStandardItemModel(0, 2, parent)
        horizontal = Qt.Orientation.Horizontal
        model.setHeaderData(self.MOVIE_TITLE_HEADING, horizontal, 'Movie')
        model.setHeaderData(self.GENRE_HEADING, horizontal, 'Genre')

        return model



    def add_movie(self, model, move_title: str, genres: str):
        model.insertRow(0)
        model.setData(model.index(0, self.MOVIE_TITLE_HEADING), move_title)
        model.setData(model.index(0, self.GENRE_HEADING), genres)


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
