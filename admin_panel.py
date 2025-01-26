import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel

from db import Database
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLineEdit, QApplication, QComboBox, \
    QGridLayout, QPushButton, QLabel, QGroupBox, QTreeView, QHBoxLayout

from main import AddMovieForm
from search_movie import SearchMovie
from window_manager import WindowManager


class AdminPanelWindow(QWidget):
    MOVIE_TITLE_HEADING, GENRE_HEADING = range(2)

    def text_changed(self, text):
        self.search.title = text
        self.populate_treeview()

    def combobox_changed(self):
        genre_text = '' if self.combobox.currentText() == 'Any' else self.combobox.currentText()
        self.search.genre = genre_text
        self.populate_treeview()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("admin panel".title())

        left, top, width, height = (10, 10, 640, 240)

        self.setGeometry(left, top, width, height)

        self.movie_title = ''
        self.genre = ''
        self.search = SearchMovie(title='', genre='', db=db)
        self.search.filter_movie()

        self.text_box = QLineEdit()
        outer_layout = QVBoxLayout()
        top_layout = QGridLayout()
        top_layout.addWidget(QLabel("Movie"), 0, 0)
        top_layout.addWidget(self.text_box, 0, 1)
        self.text_box.installEventFilter(self)
        self.text_box.textEdited.connect(self.text_changed)

        self.combobox = QComboBox()
        combobox = self.combobox
        combobox.addItem("Any")

        [combobox.addItem(row.name) for row in db.fetch_movie_genres()]
        self.combobox.activated.connect(self.combobox_changed)

        top_layout.addWidget(QLabel("Genre"), 0, 2)
        top_layout.addWidget(combobox, 0, 3)

        self.data_group_box = QGroupBox("Movies")
        self.data_view = QTreeView()
        self.data_view.setRootIsDecorated(False)
        self.data_view.setAlternatingRowColors(True)

        data_layout = QHBoxLayout()
        data_layout.addWidget(self.data_view)
        self.data_group_box.setLayout(data_layout)
        self.model = self.create_movie_model(self)
        self.data_view.setModel(self.model)
        self.populate_treeview()

        bottom_layout = QGridLayout()
        btn_add_movie = QPushButton("add movie".title())
        btn_edit_movie = QPushButton("edit movie".title())
        btn_delete_movie = QPushButton("delete movie".title())
        open_movie_window = WindowManager()
        btn_add_movie.clicked.connect(lambda x: open_movie_window.show_new_window(AddMovieForm()))

        bottom_layout.addWidget(btn_add_movie, 0, 0)
        bottom_layout.addWidget(btn_edit_movie, 0, 1)
        bottom_layout.addWidget(btn_delete_movie, 0, 2)

        middle_layout = QVBoxLayout()
        middle_layout.addWidget(self.data_group_box)

        outer_layout.addLayout(top_layout)
        outer_layout.addLayout(middle_layout)
        outer_layout.addLayout(bottom_layout)
        self.setLayout(outer_layout)

    def populate_treeview(self):
        self.model.clear()
        self.model = self.create_movie_model(self)
        self.data_view.setModel(self.model)
        for i in self.search.filter_movie():
            self.add_movie(self.model, i.get('title'), i.get('genres'))

    def create_movie_model(self, parent):
        model = QStandardItemModel(0, 2, parent)
        horizontal = Qt.Orientation.Horizontal
        model.setHeaderData(self.MOVIE_TITLE_HEADING, horizontal, 'Movie')
        model.setHeaderData(self.GENRE_HEADING, horizontal, 'Genre')
        return model

    def clear_treeview(self, model: QStandardItemModel):
        model.clear()

    def add_movie(self, model, move_title: str, genres: str):
        model.insertRow(0)
        model.setData(model.index(0, self.MOVIE_TITLE_HEADING), move_title)
        model.setData(model.index(0, self.GENRE_HEADING), genres)


def main():
    app = QApplication(sys.argv)
    window = AdminPanelWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    db = Database()
    main()
