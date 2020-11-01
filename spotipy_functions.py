import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from passwords import *  


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
    


#spotify = spotipy.Spotify(token)

def get_playlist_tracks(username,playlist_id):
    '''
    input: username and playlist id
    output: list of track ids in that playlist
    '''
    results = spotify.user_playlist_tracks(username,playlist_id)
    info = results['items']
    while results['next']:
        results = spotify.next(results)
        info.extend(results['items'])
    tracks = []
    for d in info:
        tracks += [d['track']['id']]
    return tracks

#tracks = get_playlist_tracks('aminvikram', '5agf2Irrk07oNXTMuIm0J3')

def get_playlists(username):
    '''
    input: username
    output: dictionary where the keys are playlist names and value is id for each playlist of a user
    '''
    info = spotify.user_playlists(username)
    playlist_names = []
    playlist_ids = []
    for playlist in info['items']:
        playlist_names += [playlist['name']]
        playlist_ids += [playlist['id']]
    return dict(zip(playlist_names, playlist_ids))
    
#playlists = get_playlists('aminvikram')

def build_playlist(username, track_list, playlist_name):
    '''
    inputs: username and a list of track ids
    output: nothing
    creates a playlist with the list of tracks named playlist_name
    '''
    playlist = spotify.user_playlist_create(username, playlist_name)
    spotify.user_playlist_add_tracks(username, playlist_id=playlist['id'], tracks=track_list)
    return playlist
    
#build_playlist('aminvikram', ['7jdBp6gDHrCK0YVKuqrU8d'], 'testing')

def get_song_info(id_code):
    '''
    input: song id
    output: tuple of artist and name of song
    '''
    track_info = spotify.track(id_code)
    artist_names = [artist['name'] for artist in track_info['album']['artists']]
    track_name = track_info['name']
    return artist_names[0], track_name


#print(get_song_info('7jdBp6gDHrCK0YVKuqrU8d'))

#lax playlist uri
#spotify:user:aminvikram:playlist:5agf2Irrk07oNXTMuIm0J3