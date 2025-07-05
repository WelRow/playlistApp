import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
redirectUrl = 'https://naturalsharp.net/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                                           client_secret=clientSecret,
                                                           redirect_uri=redirectUrl,
                                                           scope="user-library-read"))

def searchForAlbumCover(albumName):
    results = sp.search(q=albumName, limit=1, type="album")
    return results['albums']['items'][0]["images"][1]["url"]

results = sp.current_user_saved_tracks()
print(results)