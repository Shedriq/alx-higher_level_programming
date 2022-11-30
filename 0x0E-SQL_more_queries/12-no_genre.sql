-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres
ON tv_shows.ide = tv_show_genres.show.id
wherUe tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;