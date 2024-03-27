from ytmusic_instance import my_ytmusic
from enums import Status
import pprint


"""
to use in a try catch block
Gets the playlist id of a playlist depending on the name
"""
def get_playlist_id(name_of_playlist: str):
    playlists = my_ytmusic.get_library_playlists(limit=None);

    my_playlist_id = None
    for playlist in playlists:
        if name_of_playlist.lower() == playlist["title"].lower():
            print(f"Playlist {name_of_playlist.upper()} found...\n")
            # print(playlist)
            my_playlist_id = playlist["playlistId"];
    
    if my_playlist_id == None:
       raise Exception("Playlist not found") 
    
    return my_playlist_id


"""
this function takes two playlists id's, returns if there are duplicate songs
"""
def hasDuplicateSongs(first_playlist_id, second_playlist_id):

    print(first_playlist_id)

    # if an id is null
    if first_playlist_id == None or second_playlist_id == None:
        return Status.NULL
    
    # get playlist
    first_playlist = my_ytmusic.get_playlist(first_playlist_id, limit=None)
    second_playlist = my_ytmusic.get_playlist(second_playlist_id, limit=None)

    # if one of them come back as None
    if (not first_playlist or not second_playlist):
        return Status.NULL

    # first and second playlist are the same
    # if (first_playlist["id"] == second_playlist["id"]):
    #     return Status.IDENTICAL
    
    # get the tracks
    first_playlist_tracks = first_playlist["tracks"]
    second_playlist_tracks = second_playlist["tracks"]

    # go throguh each track and see if it exists
    for track in first_playlist_tracks:
        videoId = track["videoId"]
        for track2 in second_playlist_tracks:
            if track2["videoId"] == videoId:
                return Status.DUPLICATES_EXIST
                


id = get_playlist_id("relaxation")
s = hasDuplicateSongs(id, id)
print(s)

"""
this function returns a list of video id's that have been filtered from two playlist containing duplicate songs
"""