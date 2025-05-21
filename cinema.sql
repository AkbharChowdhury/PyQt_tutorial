CREATE OR REPLACE PROCEDURE pr_add_movie_and_genres(
	movie_title varchar,
	genres INT[]
)
AS
$body$
DECLARE
    genre int;
    movie int;

BEGIN

    INSERT INTO movies(title) VALUES (movie_title) RETURNING movie_id INTO movie;

		FOREACH genre IN ARRAY genres
		LOOP
			INSERT INTO movie_genres (movie_id, genre_id) VALUES (movie, genre);
		END LOOP;

END;
$body$
LANGUAGE PLPGSQL;


CALL pr_add_movie_and_genres('pirates', '{37,34}'::INT[]);