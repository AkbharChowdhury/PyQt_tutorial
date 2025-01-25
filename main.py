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
from genres import Genre


def get_genres():
    n = MyCounter()
    return [
        Genre('Action', n.number()),
        Genre('Adventure', n.number()),
        Genre('Animation', n.number()),
        Genre('Children', n.number()),
        Genre('Comedy', n.number()),
        Genre('Crime', n.number()),
        Genre('Documentary', n.number()),
        Genre('Drama', n.number()),
        Genre('Fantasy', n.number()),
        Genre('Horror', n.number()),
        Genre('Musical', n.number()),
        Genre('Mystery', n.number()),
        Genre('Romance', n.number()),
        Genre('Sci-Fi', n.number()),
        Genre('Thriller', n.number()),
    ]


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
    main()
