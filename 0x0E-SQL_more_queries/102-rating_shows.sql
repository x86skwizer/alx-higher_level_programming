-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rating) as rating_sum
FROM tv_shows_rate
GROUP BY title
ORDER BY rating_sum DESC;
