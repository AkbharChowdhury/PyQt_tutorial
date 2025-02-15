from dataclasses import dataclass

from PyQt6.QtWidgets import QCheckBox


@dataclass(frozen=True)
class Genre:
    name: str
    genre_id: int

    @staticmethod
    def genre_split():
        return ' | '

    @staticmethod
    def get_genres(db):
        return db.fetch_all_genres()

    @staticmethod
    def create_genre_checkboxes(self, db):
        return [QCheckBox(genre.name, self) for genre in Genre.get_genres(db)]
