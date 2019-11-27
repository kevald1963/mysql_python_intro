select Title as Album, Name as Track
from Album, Track 
where Track.AlbumId = Album.AlbumId
limit 14;