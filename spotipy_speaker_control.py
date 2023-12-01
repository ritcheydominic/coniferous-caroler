import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import util
cid = '500d52c25b89477dae46b95e7391bab5'
secret = 'ec17f112c45a42b690b17a6a5c8a2aca'

# scope to see avaiable devices and manage playback
scope = 'playlist-modify-public playlist-modify-private playlist-read-private user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri='http://localhost:8888/callback'))

# Look for a device called Spotifyd@coniferouscaroler
device_name = 'Spotifyd@coniferouscaroler'
devices = sp.devices()
for device in devices['devices']:
    if device['name'] == device_name:
        device_id = device['id']
        print(f"Found device {device_name} with id {device_id}")
        break

device_to_playlist = {
    "B0:4A:6A:98:EB:10": "https://open.spotify.com/playlist/72dZDJTedH4uwVuy7Dlpva?si=ab186ebe6f8c45d9",
    "testuser2": "https://open.spotify.com/playlist/5bK5b3kFIGRoX3hNCkmKSd?si=e6535dfe594649db",
}



# # add a public playlist to the queue
user_playlist_link = 'https://open.spotify.com/playlist/72dZDJTedH4uwVuy7Dlpva?si=ab186ebe6f8c45d9'
user_playlist_id = user_playlist_link.split('/')[-1].split('?')[0]

# get list of track uris
track_uris = []
results = sp.playlist_tracks(user_playlist_id)
tracks = results['items']
track_uris = [track['track']['uri'] for track in results['items']]

# randomize the list
random.shuffle(track_uris)

# configure queue playlist
queue_playlist_uri = 'spotify:playlist:0so5DFBpArVy7FbECcr7g2'
queue_playlist_id = queue_playlist_uri.split(':')[-1]

# clear queue playlist
results = sp.playlist_tracks(queue_playlist_id)
queue_removal_uris = [track['track']['uri'] for track in results['items']]
sp.playlist_remove_all_occurrences_of_items(queue_playlist_id, queue_removal_uris)

# add in new tracks
sp.playlist_add_items(queue_playlist_id, track_uris)

# connect to device
sp.transfer_playback(device_id=device_id)

# turn off shuffle
sp.shuffle(False, device_id=device_id)

# start playback
sp.start_playback(device_id=device_id, context_uri=queue_playlist_uri)

