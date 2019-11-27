select Title, Name
from Album join Artist
on Album.ArtistId = Artist.ArtistId
limit 5;