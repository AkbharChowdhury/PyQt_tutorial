from PyQt6.QtWidgets import QCheckBox
from pydantic import BaseModel, field_validator, Field
from uuid import uuid4


class Genre(BaseModel):
    class Config:
        frozen = True

    name: str
    genre_id: int = Field(default=str(uuid4()), gt=0)

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

my_genre = Genre(name='Horror')
print(my_genre)