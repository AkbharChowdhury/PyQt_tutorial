from PyQt6.QtWidgets import QCheckBox, QMessageBox, QLineEdit

from messageboxes import MyMessageBox


class AddMovieFormValidation:

    def clear_form(self):
        [checkbox.setChecked(False) for checkbox in self._checkbox_genres if checkbox.isChecked()]
        self.txt_movie.clear()

    def __init__(self, checkbox_genres, txt_movie: QLineEdit):
        self._checkbox_genres: list[QCheckBox | QCheckBox] = checkbox_genres
        self.txt_movie = txt_movie

    def is_valid(self):
        if self.txt_movie.text().strip() == '':
            MyMessageBox.show_message_box('Movie title is required!', QMessageBox.Icon.Critical)
            return False
        if not self._has_selected_genre():
            MyMessageBox.show_message_box('Please choose a genre!', QMessageBox.Icon.Critical)
            return False
        return True

    def _has_selected_genre(self):
        for checkbox in self._checkbox_genres:
            if checkbox.isChecked():
                return True
        return False

