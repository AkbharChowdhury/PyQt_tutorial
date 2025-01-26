import sys
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QCheckBox,
                             QWidget,
                             QVBoxLayout,
                             QComboBox,
                             QLabel,
                             QPushButton, QLineEdit)

from models.genres import Genre

class MyCounter:
    def __init__(self):
        self._num = 0

    def number(self):
        self._num += 1
        return self._num


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

class NewWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("new window".title())
class MainWindow(QMainWindow):

    def show_new_window(self):
        print('called')

    def __init__(self):
        super().__init__()


        self.setWindowTitle("New Main")



        central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Movie"))
        self.txt_movie = QLineEdit(parent=self)
        self.layout.addWidget(self.txt_movie)

        self.add_genres()

        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.combo = QComboBox(self)
        for genre in get_genres():
            self.combo.addItem(genre.name, genre.genre_id)


        btn_add_movie = QPushButton('add movie'.title(), self)
        btn_add_movie.clicked.connect(self.add_movie_clicked)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(btn_add_movie)

    def add_movie_clicked(self):

        window = NewWindow()
        window.show()

        # self.show_new_window()
        # print(self.combo.currentText())
        # print(self.combo.currentData())

    def add_genres(self):
        for genre in get_genres():
            checkbox = QCheckBox(genre.name, self)
            self.layout.addWidget(checkbox)
            # checkbox.stateChanged.connect(self.checkbox_state_changed)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    # print(get_genres().sort)
    # sample = get_genres().sort(key=lambda x: x.)
    # print(sample)
