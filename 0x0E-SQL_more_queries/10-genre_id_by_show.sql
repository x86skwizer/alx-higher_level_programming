-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_shows_genres.genre_id FROM hbtn_0d_tvshows ORDER BY tv_shows.title, tv_shows_genres.genre_id;
