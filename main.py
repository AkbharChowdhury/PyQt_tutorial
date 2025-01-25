import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox, QWidget, QVBoxLayout

from MyCounter import MyCounter
from genres import Genre





def get_genres():
    n  = MyCounter()

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
        self.setWindowTitle("Add Movie")
        central_widget = QWidget()
        layout = QVBoxLayout()

        for genre in get_genres():
            checkbox = QCheckBox(genre.name, self)
            layout.addWidget(checkbox)
            checkbox.stateChanged.connect(self.checkbox_state_changed)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def checkbox_state_changed(self, state):
        checkbox = self.sender()
        print(f"{checkbox.text()}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    # print(get_genres())
