import sys

from db import Database
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLineEdit, QApplication, QComboBox, \
    QGridLayout, QPushButton, QLabel
from search_movie import SearchMovie


class AdminPanelWindow(QWidget):

    def text_changed(self, text):
        self.search.title = text
        self.search.filter_movie()

    def combobox_changed(self):
        genre_text = '' if self.combobox.currentText() == 'Any' else self.combobox.currentText()
        self.search.genre = genre_text
        self.search.filter_movie()

    def __init__(self):
        super().__init__()
        self.movie_title = ''
        self.genre = ''
        self.search = SearchMovie(title='', genre='', db=db)
        self.search.filter_movie()
        self.setWindowTitle("admin panel".title())
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

        [combobox.addItem(row.name) for row in db.fetch_all_genres()]
        self.combobox.activated.connect(self.combobox_changed)

        top_layout.addWidget(QLabel("Genre"), 0, 2)
        top_layout.addWidget(combobox, 0, 3)

        middle_layout = QVBoxLayout()

        middle_layout.addWidget(QCheckBox("Option one"))
        middle_layout.addWidget(QCheckBox("Option two"))
        middle_layout.addWidget(QCheckBox("Option three"))

        bottom_layout = QGridLayout()

        bottom_layout.addWidget(QPushButton("add movie".title()), 0, 0)
        bottom_layout.addWidget(QPushButton("edit movie".title()), 0, 1)
        bottom_layout.addWidget(QPushButton("delete movie".title()), 0, 2)

        outer_layout.addLayout(top_layout)
        outer_layout.addLayout(middle_layout)
        outer_layout.addLayout(bottom_layout)
        self.setLayout(outer_layout)


def main():
    app = QApplication(sys.argv)
    window = AdminPanelWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    db = Database()
    # search()
    main()
