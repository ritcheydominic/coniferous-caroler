# Shows the top tracks for a user

import spotipy
from spotipy.oauth2 import SpotifyOAuth

cid = '500d52c25b89477dae46b95e7391bab5'
secret = 'ec17f112c45a42b690b17a6a5c8a2aca'
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri='http://localhost:8888/callback'))

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()