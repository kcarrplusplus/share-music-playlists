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

"
What is happenning what your request is that to add spotify URIs to a playlist you need permission from the playlist owner. This is done through using a Spotify login form that is shown as part of the authorization process using the Implicit Grant or Authorization Code flows. When implementing one of those flows you will also need to provide the right scope to perform the operation, which is playlist-modify-public or playlist-modify-private according to the documentation of the endpoint.

This library only implements the Client Credentials flow, and as such can't be used for your specific use case.

I recommend you to have a look at the authorization guide to get a better understanding of what's needed. If you plan to use node, you would like to know that there is a nodejs wrapper for the Spotify Web API that includes handy methods for the authorization process."

[user authentication issue with Spotify](https://github.com/JMPerez/spotify-web-api-token/issues/1)