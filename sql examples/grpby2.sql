select Album.AlbumId, Title as Album, Name as Track
from Album, Track 
where Track.AlbumId = Album.AlbumId
and Album.AlbumId < 5