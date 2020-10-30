import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "039dbb79401e0d93dc84766beda5251f"  # this is a sample key
API_SECRET = "2b165978821966c93a2616152d13b2ac"

# In order to perform a write operation you need to authenticate yourself
username = "aminvikram"
password_hash = pylast.md5("Tnsittpsif6!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

def get_tags(artist, name):
    track = network.get_track("Coldplay", "Yellow")
    #Get the tags a a TopItem object. 
    topItems = track.get_top_tags(limit=None)

    tags = []
    for topItem in topItems:
        tags+= [[topItem.item.get_name(), topItem.weight]]
    return tags

test = get_tags('Coldplay', 'Yellow')


