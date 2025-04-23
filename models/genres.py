from PyQt6.QtWidgets import QCheckBox
from pydantic import BaseModel, NonNegativeInt, field_validator


class Genre(BaseModel):
    class Config:
        frozen = True

    name: str
    genre_id: NonNegativeInt

    @staticmethod
    def genre_split():
        return ' | '

    @staticmethod
    def get_genres(db):
        return db.fetch_all_genres()

    @staticmethod
    def create_genre_checkboxes(self, db):
        return [QCheckBox(genre.name, self) for genre in Genre.get_genres(db)]

    @field_validator('name')
    @classmethod
    def validate_name(cls, name: str):
        if name.strip() == '':
            raise Exception('Genre cannot be empty')
        return name


genre = Genre(name='', genre_id=0)
print(genre.model_dump())
