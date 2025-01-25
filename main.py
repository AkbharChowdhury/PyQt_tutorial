import sys
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QCheckBox,
                             QWidget,
                             QVBoxLayout,
                             QLabel,
                             QPushButton,
                             QLineEdit
                             )

from MyCounter import MyCounter
from db import Database
from genres import Genre


def get_genres():
    # return [Genre(row[0], row[1]) for row in db.fetch_all_genres()]
    return db.fetch_all_genres()



class MainWindow(QMainWindow):

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
        print("selected genres: ")
        print('---------')
        selected_genres = [checkbox.text() for checkbox in self.genre_checkboxes if checkbox.isChecked()]
        print(selected_genres)
        selected_genre_ids = set(genre.genre_id for genre in get_genres() if genre.name in selected_genres)
        print("selected genre IDs: ")
        print(selected_genre_ids)

    def create_genre_checkboxes(self):
        return [QCheckBox(genre.name, self) for genre in get_genres()]


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    db = Database()
    main()
