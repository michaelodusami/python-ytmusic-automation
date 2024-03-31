"""
File: backend_playlist.py
Description: backend module responsible for interacting directly with the yt music instance | account
@author: Michael-Andre Odusami
@version: March 2024
"""


from ytmusic_instance import my_ytmusic
import pprint

def add_playlist_songs_to_playlist_with_list_of_video_id(playlist_id: str, list_of_songs: list, title_of_source: str):
    status = my_ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=list_of_songs)
    # printStatus(status)
    return f"Songs added from playlist : {title_of_source}"


# def printStatus(status : str | dict):
#     pprint.pprint(status)

def get_playlist(playlist_id : str):
    return my_ytmusic.get_playlist(playlistId=playlist_id)

def get_all_playlists():
    return my_ytmusic.get_library_playlists(limit=None)

def get_playlist_id(name_of_playlist: str):
    """
    Gets the playlist id of a playlist depending on the name
    
    :param name_of_playlist: The name of the playlist to find the ID for.
    :type name_of_playlist: str
    :return: The ID of the playlist.
    :rtype: str
    :raises Exception: If the playlist with the given name is not found.
    """
    playlists = my_ytmusic.get_library_playlists(limit=None);

    my_playlist_id = None
    for playlist in playlists:
        if name_of_playlist.lower() == playlist["title"].lower():
            my_playlist_id = playlist["playlistId"];
    
    if my_playlist_id == None:
       raise Exception("Playlist not found") 
    
    return my_playlist_id

def get_playlist_tracks(playlist_id : str):
    """
    Retrieves the tracks of a playlist given its ID.
    
    :param playlist_id: The ID of the playlist to retrieve tracks from.
    :type playlist_id: str
    :return: The tracks of the playlist.
    :rtype: list
    :raises Exception: If the playlist ID is None or empty.
    """
    if playlist_id == None:
        raise Exception("Playlist ID is null <playlist_id = None>")
    if not playlist_id:
        raise Exception("Playlist ID is null <playlist_id = None>")
    playlist = my_ytmusic.get_playlist(playlistId=playlist_id, limit=None)
    return playlist["tracks"]

def find_unique_songs_for_playlist(destination_id : str, source_id : str):
    """
    Issue Solved: two playlist cannot include the same songs or video id's
    This function returns a list of song id's that are not in the destination playlist to be added to the destination 
    playlist
    :param destination_id : id of the playlist to add to
    :param source_id : id of the playlist you want to add to the destination
    :return list of song id's not in the destination playlist
    """
    try:
        # Assuming you have some way to get the list of song/video IDs for each playlist
        destination_songs = get_playlist_tracks(destination_id)
        source_songs = get_playlist_tracks(source_id)
        list_of_unique_songs = []
        # Find the unique songs in the source playlist
        for source_track in source_songs:
            # get the video id in the source
            source_video_id = source_track["videoId"]
            flag = False
            # loop through all destinations and count the frequency
            for destination_track in destination_songs:
                destination_video_id = destination_track["videoId"]
                if source_video_id == destination_video_id:
                    flag = True
            if flag == False:
                list_of_unique_songs.append(source_video_id)
        
        return list(set(list_of_unique_songs))
    except Exception as e:
        print(e)

def create_playlist(title = "New Playlist", description = ""):
    """
    Creates a new playlist for the user
    """
    status = my_ytmusic.create_playlist(title=title, description=description)
    return "Playlist Created"

def delete_playlist(playlist_id : str):
    status = my_ytmusic.delete_playlist(playlistId=playlist_id)
    return "Playlist has been deleted."

def rename_playlist(playlist_id : str, title : str ):
    status = my_ytmusic.edit_playlist(playlistId=playlist_id, title=title)
    return "Playlist Has Been Renamed."

def get_song_information(name_of_song: str):
    results = my_ytmusic.search(name_of_song, filter="songs", limit=1)
    return results[0]

def remove_song_from_playlist(playlist_id: str, songs: list):
    my_ytmusic.remove_playlist_items(playlistId=playlist_id, videos=songs)
    return "Songs Removed"