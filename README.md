# Music Playlist Copier
## Copy playlists between music services

## Steps:
- Ask client to provide authorization for both services to retrive playlist from old service to new service
- GET playlist metadata (song title, artist) 
- POST and create new playlist on new service

## Decisions 
- Use App or User authorization for APIs

## GET resources
- Spotify 
- Apple
- Youtube Music

## POST (create) resources
- Spotify
- Apple
- Youtube Music


## Other potential resources
- Amazon music
- Soundcloud


Research:
[Exploring the Spotify API with Python](https://stmorse.github.io/journal/spotify-api.html)