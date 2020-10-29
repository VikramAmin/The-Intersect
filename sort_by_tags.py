import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from passwords import *  
import pylast
from spotipy_functions import get_song_info, get_playlists, get_playlist_tracks
from lastfm_functions import get_tags

redirectURL = 'http://localhost/' # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/
scope = 'playlist-modify-public'
username = 'aminvikram'



client_credentials_manager = SpotifyClientCredentials(client_id=clientID,
                                                      client_secret=clientSecret)

token = util.prompt_for_user_token(username, scope, client_id=clientID, client_secret=clientSecret, redirect_uri = redirectURL, cache_path = None)


if token:
    spotify = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
    



def get_common_keys(username):
    '''
    input: username of the user
    output: dictionary where the tags are the keys and the values in number of occurances
    '''
    tags = []
    
    playlists = get_playlists(username)
    for key in playlists:
        playlist_id = playlists[key]
        tracks = get_playlist_tracks(username,playlist_id)
        for track in tracks:
            info = get_song_info(track)
            print(info[1])
            try:
                tags += get_tags(info[0], info[1])
            except:
                None
            
    
    tags = dict((x,tags.count(x)) for x in set(tags))
    return tags

#test = get_common_keys('aminvikram')
    

#Not Complete
def sort(username, tags):
    '''
    input: username and list of tags for playlists to sort into
    output: none
    sorts every song in a users library into playlists defined by tags
    '''
    playlists = get_playlists(username)
    for key in playlists:
        playlist_id = playlists[key]
        tracks = get_playlist_tracks(username,playlist_id)
        for track in tracks:
            info = get_song_info(track)
            print(info[1])
            tags = []
            try:
                tags += get_tags(info[0], info[1])
            except:
                None
            for tag in tags:
                
    
    