-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT name
FROM tv_genres
WHERE id NOT IN (SELECT genre_id FROM tv_show_genres WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter'))
ORDER BY name ASC;
