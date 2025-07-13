import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

class SpotifyClient:
    def __init__(self, redirect_uri='https://naturalsharp.net/'):
        
        
        load_dotenv()
        clientID = os.getenv("CLIENT_ID")
        clientSecret = os.getenv("CLIENT_SECRET")

        scope = "user-library-read playlist-read-private"

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=clientID,
                client_secret=clientSecret,
                redirect_uri=redirect_uri,
                scope=scope
            )
        )

    def searchForAlbumCover(self, albumName):
        results = self.sp.search(q=albumName, limit=1, type="album")
        return results['albums']['items'][0]["images"][1]["url"]
    
    def getCurrentUserPlaylists(self, limit=20):
        return self.sp.current_user_playlists(limit=limit)

if __name__ == "__main__":
    try:
        # 1. Create an instance of the client
        spotify_client = SpotifyClient()

        # 2. Get and print the user's playlists
        print("\nFetching your playlists...")
        playlists_data = spotify_client.getCurrentUserPlaylists(limit=10)
        
        if playlists_data and playlists_data['items']:
            print("Found your playlists:")
            for i, playlist in enumerate(playlists_data['items']):
                print(f"  {i + 1}. {playlist['name']} ({playlist['tracks']['total']} tracks)")
        else:
            print("Could not find any playlists or you have no playlists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")