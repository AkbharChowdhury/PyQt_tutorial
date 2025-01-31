class MovieInfo:
    MOVIE_ID = 0
    MOVIE_SORTED = None

    @staticmethod
    def sort_movie(movies: list[dict[str, str]], column: str):
        return sorted(movies, key=lambda d: d.get(column))

