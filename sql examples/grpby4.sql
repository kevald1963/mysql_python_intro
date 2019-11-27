select Album.AlbumId, Album.Title, count(*)
from Album, Track 
where Track.AlbumId = Album.AlbumId
and Album.AlbumId < 5
group by Album.AlbumId;