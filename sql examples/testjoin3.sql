select Name as Track, Title as Album, ArtistID
from Track, Album
where Track.AlbumId = Album.AlbumId
/* limit 5;