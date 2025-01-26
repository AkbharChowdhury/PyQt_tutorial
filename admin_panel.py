import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QApplication, QComboBox, \
    QGridLayout, QPushButton, QLabel, QGroupBox, QTreeView, QHBoxLayout

from db import Database
from main import AddMovieForm
from models.movie_table import MovieTable, MovieColumn
from search_movie import SearchMovie
from window_manager import WindowManager


class AdminPanelWindow(QWidget):

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

        self.movie_title = self.genre = ''
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
        self.combobox.addItem("Any")
        [self.combobox.addItem(row.name) for row in db.fetch_movie_genres()]
        self.combobox.activated.connect(self.combobox_changed)

        top_layout.addWidget(QLabel("Genre"), 0, 2)
        top_layout.addWidget(self.combobox, 0, 3)

        self.data_group_box = QGroupBox("Movies")
        self.table = QTreeView()

        self.table.setRootIsDecorated(False)
        self.table.setAlternatingRowColors(True)

        data_layout = QHBoxLayout()
        data_layout.addWidget(self.table)
        self.data_group_box.setLayout(data_layout)
        self.movie_table = MovieTable()
        self.model = None
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
        self.model = self.movie_table.create_model(self)
        self.table.setModel(self.model)
        for movie in self.search.filter_movie():
            movie_data = {
                MovieColumn.MOVIE.name: movie.get('title'),
                MovieColumn.GENRE.name: movie.get('genres')
            }
            MovieTable.add_movie(self.model, movie_data)


def main():
    app = QApplication(sys.argv)
    window = AdminPanelWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    db = Database()
    main()
