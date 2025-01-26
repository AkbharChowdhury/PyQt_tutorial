from dataclasses import dataclass


@dataclass(frozen=True)
class Genre:
    name: str
    genre_id: int
    @staticmethod
    def genre_split():
        return ' | '
