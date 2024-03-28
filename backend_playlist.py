from ytmusic_instance import my_ytmusic
import backend_utility
import pprint
from enums import Status

def add_playlist_songs_to_playlist(playlist_id : str, source_playlist_id: str):
    status = my_ytmusic.add_playlist_items(playlistId=playlist_id, source_playlist=source_playlist_id, duplicates=True)
    if status["status"] == "STATUS_FAILED":
        print("Song Addition Failed... Printing Returning Object Of Failiure")
        pprint.pprint(status)
    else:
        print("Song Addition Success...")



"""
this function returns a list of video id's that have been filtered from two playlist containing duplicate songs
"""
def getFilteredSongsFromDuplicatePlaylist(first_playlist_id, second_playlist_id): 
        # get the playlists
        try:
            first_playlist_tracks = backend_utility.get_playlist_tracks(first_playlist_id)
            second_playlist_tracks = backend_utility.get_playlist_tracks(second_playlist_id)
            list_of_duplicate_ids = set()

            # get the duplicate keys
            for track in first_playlist_tracks:
                videoId = track["videoId"]
                for track2 in second_playlist_tracks:
                    if track2["videoId"] == videoId:
                        list_of_duplicate_ids.add(videoId)
            
            # get the non dupes from both tracks
            list_of_non_dupes = list()
            for track in first_playlist_tracks:
                videoId = track["videoId"]
                if videoId in list_of_duplicate_ids:
                    continue
                list_of_non_dupes.append(videoId)
            
            return list_of_non_dupes
        except Exception as e:
            print(e)



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
    if (first_playlist_id == second_playlist_id):
        return Status.IDENTICAL
    
    # get the tracks
    first_playlist_tracks = get_playlist_tracks(first_playlist_id)
    second_playlist_tracks = get_playlist_tracks(second_playlist_id)

    # go throguh each track and see if it exists
    for track in first_playlist_tracks:
        videoId = track["videoId"]
        for track2 in second_playlist_tracks:
            if track2["videoId"] == videoId:
                return Status.DUPLICATES_EXIST
                


        


def get_playlist_tracks(playlist_id):
    if playlist_id == None:
        raise Exception("Playlist ID is null <playlist_id = None>")
    if not playlist_id:
        raise Exception("Playlist ID is null <playlist_id = None>")
    playlist = my_ytmusic.get_playlist(playlistId=playlist_id, limit=None)
    return playlist["tracks"]
