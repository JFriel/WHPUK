import spotipy
import sys
import spotipy.util as util
import os

def run(se):
	f = se
	os.environ['SPOTIPY_CLIENT_ID'] = 'ac497bd019ae4c84b33cb54c615496a7'
	os.environ['SPOTIPY_CLIENT_SECRET'] = '3353544aa8344e50927459f630ac8704'
	os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'

	def add(serch):
	    if len(serch) > 1:
	        username = "1119587538"
	        playlist_id = "47dWRITq7VKBROxfhwFTAk"
	        track_ids = search(serch) 
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
	       
	def search(serch):
	    tracks = ' '.join(serch[1:])
	    tracks = spotipy.Spotify().search(q=tracks, limit=1)
	    for i,t in enumerate(tracks['tracks']['items']):
	        tracks = t['id']
	    return tracks
	        
	add(f)

