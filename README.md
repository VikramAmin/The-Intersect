# The-Intersect
Uses Spotipy to allow the user to create playlist out of the intersection of two playlists.
Also using crowd sourced tags from lastfm to classify the mood and/or of individual songs.

Goal: 
1. To create a system that allows a user to preform intersections and unions for playlists
2. To allow a user to build playlists by using keywords of decade, mood, and genre

To Do:
- [x] Build wraper functions for api calls for both Spotify and Lastfm
- [ ] Build function that creates a playlist from the intersection of two playlists
- [ ] Build function that creates a playlist from the union of two playlists
- [ ] Build NLP function that builds a mood vector from the top tags of a song on Lastfm
- - [ ] Choose what set of moods to use as a basis for the vector space of moods (model of Henver vs Russel)
- - [ ] train or find a trained model for music genres
- [ ] Build function that gets the genre of a given song (using either Spotify's artist/album tags or Lastfm)
- [ ] Build function that takes a list of years, genres, and moods and builds a playlist
- [ ] Build user interface and make it easily likable to any spotify account
- [ ] Explore options of getting it to work with voice assistants
