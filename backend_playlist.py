from ytmusic_instance import my_ytmusic
import pprint
from enums import Status
from typing import Union

def add_playlist_songs_to_playlist(playlist_id: str, source_playlist_id_or_list: Union[str, list]):
    if isinstance(source_playlist_id_or_list, str):
        status = my_ytmusic.add_playlist_items(playlistId=playlist_id, source_playlist=source_playlist_id_or_list, duplicates=True)
    elif isinstance(source_playlist_id_or_list, list):
        status = my_ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=source_playlist_id_or_list, duplicates=True)
    else:
        raise ValueError("Invalid type for source_playlist_id_or_list")

    printStatus(status)


def printStatus(status):
    if status["status"] == "STATUS_FAILED":
        print("Song Addition Failed... Printing Returning Object Of Failiure")
        pprint.pprint(status)
    else:
        print("Song Addition Success...")


"""
this function returns a list of video id's that have been filtered from two playlist containing duplicate songs
"""
def getFilteredSongsFromDuplicatePlaylist(first_playlist_id : str, second_playlist_id : str): 
        # get the playlists
        try:
            first_playlist_tracks = get_playlist_tracks(first_playlist_id)
            second_playlist_tracks = get_playlist_tracks(second_playlist_id)
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

def getNonDuplicatedSongsFromPlaylist(id):
    tracks = get_playlist_tracks(id)
    track_frequency = dict()
    for track in tracks:
        videoId = track["videoId"]
        found = False
        for trackToCheck in tracks:
            if videoId == trackToCheck["videoId"]:
                if videoId not in track_frequency:
                    track_frequency[videoId] = 0
                else:
                    track_frequency[videoId] += 1
    non_duplicated_ids = []
    for video_id, freq in track_frequency.items():
        if freq == 0:
            non_duplicated_ids.append(video_id)
    
    return non_duplicated_ids


"""
to use in a try catch block
Gets the playlist id of a playlist depending on the name
"""
def get_playlist_id(name_of_playlist: str):
    playlists = my_ytmusic.get_library_playlists(limit=None);

    my_playlist_id = None
    for playlist in playlists:
        if name_of_playlist.lower() == playlist["title"].lower():
            my_playlist_id = playlist["playlistId"];
    
    if my_playlist_id == None:
       raise Exception("Playlist not found") 
    
    return my_playlist_id


"""
this function takes two playlists id's, returns if there are duplicate songs
"""
def hasDuplicateSongs(first_playlist_id : str, second_playlist_id : str):
    # if (first_playlist_id == second_playlist_id):
    #     return Status.IDENTICAL
    
    # get the tracks
    first_playlist_tracks = get_playlist_tracks(first_playlist_id)
    second_playlist_tracks = get_playlist_tracks(second_playlist_id)

    # go throguh each track and see if it exists
    for track in first_playlist_tracks:
        videoId = track["videoId"]
        for track2 in second_playlist_tracks:
            if track2["videoId"] == videoId:
                return Status.DUPLICATES_EXIST

    return Status.DUPLICATES_DNE


        


def get_playlist_tracks(playlist_id : str):
    if playlist_id == None:
        raise Exception("Playlist ID is null <playlist_id = None>")
    if not playlist_id:
        raise Exception("Playlist ID is null <playlist_id = None>")
    playlist = my_ytmusic.get_playlist(playlistId=playlist_id, limit=None)
    return playlist["tracks"]
