# native libraries
import os

# local libraries
from spotify import Spotify

# third party libraries
from dotenv import load_dotenv
load_dotenv()

spotify = Spotify(
    client_id = os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET") 
)

spotify_current_user = os.getenv("SPOTIFY_USER_ID")

spotify.authorization()
spotify.get_current_users_playlists(spotify_current_user)
spotify.get_current_users_info(spotify_current_user)

spotify.create_playlist(spotify_current_user, 'Italian coastline under the moonlight', 'a playlist for the riveria')

