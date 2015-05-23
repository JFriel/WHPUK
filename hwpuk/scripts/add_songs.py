import spotipy
import sys
import spotipy.util as util
import os

def run():

	os.environ['SPOTIPY_CLIENT_ID'] = 'ac497bd019ae4c84b33cb54c615496a7'
	os.environ['SPOTIPY_CLIENT_SECRET'] = '3353544aa8344e50927459f630ac8704'
	os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'

	def add():
	    if len(sys.argv) > 1:
	        username = "1145201912"
	        playlist_id = "6KWAhvz9PxGuqLs0Gmde8U"
	        track_ids = search() 
	    else:
	        print "Blank Space isn't on Spotify anymore."
	        sys.exit()
	    scope = 'playlist-modify-public'
	    token = util.prompt_for_user_token(username, scope)
	    if token:
	        sp = spotipy.Spotify(auth=token)
	        sp.trace = False
	        results = sp.user_playlist_add_tracks(username, playlist_id, [track_ids])
	        print results
	    else:
	        print "Can't get token for", username
	       
	def search():
	    tracks = ' '.join(sys.argv[1:])
	    tracks = spotipy.Spotify().search(q=tracks, limit=1)
	    for i,t in enumerate(tracks['tracks']['items']):
	        tracks = t['id']
	    return tracks
	        
	add()
