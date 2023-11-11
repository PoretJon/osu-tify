import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from datetime import date



scope = 'playlist-modify-public'
username = os.getenv("SPOT_NAME")


token = SpotifyOAuth(scope=scope, username=username)

sp = spotipy.Spotify(auth_manager=token)


osu_user = 'Mizora'

playlist_name = osu_user + "'s Top Plays"
playlist_desc = "Top plays of osu! player", osu_user

sp.user_playlist_create(user=username, name=playlist_name, public=True, collaborative=False, description=playlist_desc)



