select Title, Name
from Album, Artist
where Album.ArtistId = Artist.ArtistId
limit 5;