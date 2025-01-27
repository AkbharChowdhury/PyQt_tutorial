import sys
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QVBoxLayout,
                             QLabel,
                             QPushButton,
                             QLineEdit, QMessageBox
                             )

import admin_panel
from models.genres import Genre
from utils.form_validation import AddMovieFormValidation
from utils.messageboxes import MyMessageBox
from database import Database
from window_manager import WindowManager


class AnotherWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Movie".title())


class AddMovieForm(QMainWindow):
    def show_new_window(self, win):
        self.w = win
        self.w.show()
    def window_action(self):
        if WindowManager.has_closed_admin_panel():
            self.show_new_window(admin_panel.AdminPanelWindow())


    def __init__(self):
        super().__init__()
        self.open_admin_panel = WindowManager()

        self.db = Database()

        self.setWindowTitle("Add Movie".title())
        central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Movie"))
        self.txt_movie = QLineEdit(self)
        self.layout.addWidget(self.txt_movie)
        self.genre_checkboxes = Genre.create_genre_checkboxes(self, self.db)

        [self.layout.addWidget(genre_checkbox) for genre_checkbox in self.genre_checkboxes]
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        btn_add_movie = QPushButton('add movie'.title(), self)
        btn_add_movie.clicked.connect(self.movie_button_action)
        self.layout.addWidget(btn_add_movie)

    def movie_button_action(self):
        db = self.db
        form = AddMovieFormValidation(self.genre_checkboxes, self.txt_movie)
        if not form.is_valid(): return
        selected_genres = [checkbox.text() for checkbox in self.genre_checkboxes if checkbox.isChecked()]
        genre_id_list = set(genre.genre_id for genre in Genre.get_genres(db) if genre.name in selected_genres)
        last_inserted_movie_id = db.add_movie(self.txt_movie.text())
        db.add_movie_genres(last_inserted_movie_id, genre_id_list)
        form.clear_form()
        MyMessageBox.show_message_box('Movie Added', QMessageBox.Icon.Information)
        self.window_action()


def main():
    app = QApplication(sys.argv)
    window = AddMovieForm()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    db = Database()
    movies = db.fetch_movies(genre='romance')
    main()
