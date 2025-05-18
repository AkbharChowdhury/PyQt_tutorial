CREATE OR REPLACE PROCEDURE pr_add_movie_and_genres(
	movie_title varchar,
	genres INT[]
)
AS
$body$
DECLARE
    genre_id_index int;
    inserted_movie_id INT;

BEGIN

    INSERT INTO movies(title) VALUES (movie_title) RETURNING movie_id INTO inserted_movie_id;

		FOREACH genre_id_index IN ARRAY genres
		LOOP
			INSERT INTO movie_genres (movie_id, genre_id) VALUES (inserted_movie_id, genre_id_index);
		END LOOP;

END;
$body$
LANGUAGE PLPGSQL;


CALL pr_add_movie_and_genres('pirates', '{37,34}'::INT[]);