import sys
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QCheckBox,
                             QWidget,
                             QVBoxLayout,
                             QLabel,
                             QPushButton,
                             QLineEdit, QMessageBox
                             )

from db import Database
from form_validation import AddMovieFormValidation
from messageboxes import MyMessageBox


def get_genres():
    return db.fetch_all_genres()


class AddMovieForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Movie".title())
        central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Movie"))
        self.txt_movie = QLineEdit(self)
        self.layout.addWidget(self.txt_movie)
        self.genre_checkboxes = self.create_genre_checkboxes()
        [self.layout.addWidget(genre_checkbox) for genre_checkbox in self.genre_checkboxes]
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        btn_add_movie = QPushButton('add movie'.title(), self)
        btn_add_movie.clicked.connect(self.movie_button_action)

        self.layout.addWidget(btn_add_movie)


    def movie_button_action(self):
        form = AddMovieFormValidation(self.genre_checkboxes, self.txt_movie)
        if not form.is_valid(): return
        selected_genres = [checkbox.text() for checkbox in self.genre_checkboxes if checkbox.isChecked()]
        genre_id_list = set(genre.genre_id for genre in get_genres() if genre.name in selected_genres)
        last_inserted_movie_id = db.add_movie(self.txt_movie.text())
        db.add_movie_genres(last_inserted_movie_id, genre_id_list)
        form.clear_form()
        MyMessageBox.show_message_box('Movie Added', QMessageBox.Icon.Information)

    def create_genre_checkboxes(self):
        return [QCheckBox(genre.name, self) for genre in get_genres()]


def main():
    app = QApplication(sys.argv)
    window = AddMovieForm()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    db = Database()
    main()
