-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL

SELECT s.title, g.genre_id 
FROM tv_shows s 
LEFT JOIN tv_show_genres g ON s.id = g.show_id 
WHERE g.show_id IS NULL 
ORDER BY s.title, g.genre_id ASC;
