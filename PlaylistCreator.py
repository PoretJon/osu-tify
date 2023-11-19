from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from datetime import date
from dotenv import load_dotenv

load_dotenv()


# TODO: Create a better way to add songs to a playlist
#   Currently, I am just searching using the name and artist in and adding the first song.
#   There are some songs on osu! that have incorrect spellings/grammar in the names of artists.
#       (ex: Black Rover has the artist written as "Vickeblanka" on most mapsets while on spotify its written as "Vicke Blanka")
# TODO: create a database of spotify artist URIs
#   currently, the program just searches based on song name and artist. I want to eventually have a database of
#   artists and spotify URI's that gets automated so its easier to look for songs

class SpotifyComponent():
    def __init__(self):
        self.scope = 'user-modify-playback-state playlist-modify-public'
        self.username = getenv('SPOT_NAME')

        self.token = SpotifyOAuth(scope=self.scope, username=self.username, client_id=getenv('SPOTIPY_CLIENT_ID'), client_secret=getenv('SPOTIPY_CLIENT_SECRET'))
        self.spotifyClient = spotipy.Spotify(auth_manager=self.token)

    def add_songs_to_playback(self, songs):
        for song in songs:
            print("Adding", song.title, "to playback queue")
            result = self.spotifyClient.search(q=(str(song.artist,song.track)))
            song = result['tracks']['items'][0]['uri']
            self.spotifyClient.add_to_queue(song)

    def create_playlist(self,songs):
         for song in songs:
            print("Adding", song.title, "to playlist")
            result = self.spotifyClient.search(q=(str(song.artist,song.track)))
            if len(result) < 1:
                print("couldnt find song, skipping")
                continue
            song = result['tracks']['items'][0]['uri']


