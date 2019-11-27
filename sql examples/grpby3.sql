select count(*)
from Album, Track 
where Track.AlbumId = Album.AlbumId
and Album.AlbumId < 5
group by Album.AlbumId;