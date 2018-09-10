import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "edf8b90258cc6472922ade7541fc0c79"  # this is a sample key
API_SECRET = "73ec7f7d13626220aff436d86192399f"

# In order to perform a write operation you need to authenticate yourself
username = "aminvikram"
password_hash = pylast.md5("tnsittpsif6!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

def get_tags(artist, name):
    track = network.get_track(artist, name)
    top_tags = track.get_top_tags()
    tags = []
    for e in top_tags:
        tags += [e[0].name]
    return tags

tags = get_tags('Coldplay', 'Clocks')
