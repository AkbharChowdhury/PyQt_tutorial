import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QApplication, QComboBox, \
    QGridLayout, QPushButton, QLabel, QGroupBox, QTreeView, QHBoxLayout, QMessageBox

import edit_movie_form
from add_movie_form import AddMovieForm
from models.movie_table import MovieTable, MovieColumn
from movie import MovieInfo
from search_movie import SearchMovie
from utils.messageboxes import MyMessageBox
from window_manager import WindowManager
from database import Database


class AdminPanelWindow(QWidget):
    def edit_movie(self):
        self.movies = self.db.fetch_movies()

        index = self.get_selected_table_index()
        selected_index = index - 1 if self.has_deleted_movie else index
        MovieInfo.MOVIE_ID = self.movies[selected_index].get('movie_id')
        self.open_edit_movie_window = WindowManager()
        self.open_edit_movie_window.show_new_window(edit_movie_form.EditMovieForm())

    def text_changed(self, text):
        self.search.title = text
        self.populate_table()

    def combobox_changed(self):
        genre_text = '' if self.combobox.currentText() == SearchMovie.all_genres() else self.combobox.currentText()
        self.search.genre = genre_text
        self.populate_table()

    def delete_movie(self):

        if not self.tree.selectedIndexes():
            MyMessageBox.show_message_box('Please choose a movie from the table', QMessageBox.Icon.Warning)
            return

        if MyMessageBox.confirm(self, 'Are you sure you want to delete this movie?') == QMessageBox.StandardButton.Yes:
            index = self.get_selected_table_index()
            self.db.delete('movie_id', 'movies', self.movies[index].get('movie_id'))
            self.tree.model().removeRow(index)
            self.has_deleted_movie = True

    def get_selected_table_index(self):
        return self.tree.selectedIndexes()[0].row()

    def __init__(self):
        super().__init__()
        self.db = Database()
        self.movies = self.db.fetch_movies()
        self.movies.reverse()

        self.has_deleted_movie = False

        self.setWindowTitle("admin panel".title())

        left, top, width, height = (10, 10, 640, 450)

        self.setGeometry(left, top, width, height)

        self.movie_title = self.genre = ''
        self.search = SearchMovie(title='', genre='', db=self.db)
        self.search.filter_movie()

        self.text_box = QLineEdit()
        outer_layout = QVBoxLayout()
        top_layout = QGridLayout()
        top_layout.addWidget(QLabel("Movie"), 0, 0)
        top_layout.addWidget(self.text_box, 0, 1)
        self.text_box.installEventFilter(self)
        self.text_box.textEdited.connect(self.text_changed)

        self.combobox = QComboBox()
        self.combobox.addItem(SearchMovie.all_genres())
        [self.combobox.addItem(row.name) for row in self.db.fetch_movie_genres()]
        self.combobox.activated.connect(self.combobox_changed)

        top_layout.addWidget(QLabel("Genre"), 0, 2)
        top_layout.addWidget(self.combobox, 0, 3)

        self.data_group_box = QGroupBox("Movies")
        self.tree = QTreeView()
        self.tree.setRootIsDecorated(False)
        self.tree.setAlternatingRowColors(True)

        data_layout = QHBoxLayout()
        data_layout.addWidget(self.tree)
        self.data_group_box.setLayout(data_layout)
        self.movie_table = MovieTable()
        self.model = None
        self.populate_table()

        bottom_layout = QGridLayout()
        btn_add_movie = QPushButton("add movie".title())
        btn_edit_movie = QPushButton("edit movie".title())
        btn_delete_movie = QPushButton("delete movie".title())
        open_movie_window = WindowManager()
        self.open_edit_movie_window = WindowManager()

        btn_add_movie.clicked.connect(lambda x: open_movie_window.show_new_window(AddMovieForm()))
        btn_delete_movie.clicked.connect(self.delete_movie)
        btn_edit_movie.clicked.connect(self.edit_movie)

        # btn_edit_movie.clicked.connect(lambda x: open_edit_movie_window.show_new_window(EditMovieForm()))
        bottom_layout.addWidget(btn_add_movie, 0, 0)
        bottom_layout.addWidget(btn_edit_movie, 0, 1)
        bottom_layout.addWidget(btn_delete_movie, 0, 2)

        middle_layout = QVBoxLayout()
        middle_layout.addWidget(self.data_group_box)

        outer_layout.addLayout(top_layout)
        outer_layout.addLayout(middle_layout)
        outer_layout.addLayout(bottom_layout)
        self.setLayout(outer_layout)
        self.tree.setColumnWidth(0, 300)
        self.tree.setColumnWidth(1, 300)

    def populate_table(self):
        self.model = self.movie_table.create_model(self)
        self.tree.setModel(self.model)
        for movie in self.search.filter_movie():
            movie_data = {
                MovieColumn.MOVIE.name: movie.get('title'),
                MovieColumn.GENRE.name: movie.get('genres'),
            }

            MovieTable.add_movie(self.model, movie_data)


def main():
    app = QApplication(sys.argv)
    window = AdminPanelWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
