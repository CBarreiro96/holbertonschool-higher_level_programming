-- List all shows and genres linked to show from 'hbtn_0d_tvshows'
-- If show doesn't have a genre, display NULL in genre column
-- Each record should display tv_shows.title, tv_genres.name
-- Results must be sorted in ascending order by show title
-- You can only use one SELECT statement
SELECT sh.title, gr.name FROM tv_shows AS sh
       LEFT JOIN tv_show_genres AS shgr
       ON sh.id=shgr.show_id
       LEFT JOIN tv_genres AS gr
       ON shgr.genre_id=gr.id
       ORDER BY sh.title, gr.name ASC;
