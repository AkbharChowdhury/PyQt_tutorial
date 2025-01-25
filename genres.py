from dataclasses import dataclass

@dataclass(frozen=True)
class Genre:
    name: str
    genre_id: int


def main():
    genres = [
        Genre('Action', 2),
        Genre('Children', 23)
    ]

    [print(f'Genre: {genre.name}, GenreID: {genre.genre_id}') for genre in genres]


if __name__ == '__main__':
    main()

