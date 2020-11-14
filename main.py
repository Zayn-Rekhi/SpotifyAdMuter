from spotipy.oauth2 import SpotifyOAuth
import spotipy
import time
import os

volumeLevel = input("Volume Level: ")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="01092811967a457ba2e4ab6a7434189f",
                                               client_secret="1f221bd1f02347858bbbd7d4379b27ba",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-currently-playing"))

def increaseVolume(level):
    os.popen(f"amixer sset 'Master' {level}%")
#
def setVolumeToOff():
    os.popen("amixer sset 'Master' 0%")

while True:
    results = sp.currently_playing()["currently_playing_type"]
    if results == "ad": setVolumeToOff()
    else: increaseVolume(volumeLevel)
    time.sleep(3)
