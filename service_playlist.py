"""
File: service_playlist.py
Description: Controller module responsible for managing user interactions and API connections related to playlists.
@author: Michael-Andre Odusami
@version: March 2024
"""

import backend_playlist 
from enums import Status

def add_songs_from_existing_playlist_to_other_playlist_service(destination_playlist_name, source_playlist_name):
    """
    Adds songs from one existing playlist to another playlist.

    Parameters:
    - destination_playlist_name (str): The name of the destination playlist where songs will be added.
    - source_playlist_name (str): The name of the source playlist from which songs will be copied.

    Raises:
    - Exception: If an error occurs during the process of adding songs to the destination playlist.

    Note:
    - This function relies on the 'backend_utility' module to retrieve playlist IDs.
    - The 'add_playlist_songs_to_playlist' function is used to add songs to the destination playlist.

    Example:
    add_songs_from_existing_playlist_to_other_playlist("My Favorite Songs", "Best of 2023")
    """
    try:
        # Retrieve playlist IDs
        destination_playlist_id = backend_playlist.get_playlist_id(destination_playlist_name)
        source_playlist_id = backend_playlist.get_playlist_id(source_playlist_name)

        responseStatus = backend_playlist.hasDuplicateSongs(first_playlist_id=destination_playlist_id, 
                                               second_playlist_id=source_playlist_id)

        # check for duplicates
        if responseStatus == Status.DUPLICATES_EXIST:
            list_of_song_ids = backend_playlist.getFilteredSongsFromDuplicatePlaylist(first_playlist_id=destination_playlist_id, second_playlist_id=source_playlist_id)
            if (list_of_song_ids):
                backend_playlist.add_playlist_songs_to_playlist(playlist_id=destination_playlist_id, source_playlist_id_or_list=list_of_song_ids)
            else:
                print("No songs to add to the playlist")
        elif responseStatus == Status.IDENTICAL:
            print("Playlists are identical. No need to add. Returning...")
        else:
            # Add songs to the destination playlist
            backend_playlist.add_playlist_songs_to_playlist(playlist_id=destination_playlist_id,  source_playlist_id_or_list=source_playlist_id)
    
    except Exception as e:
        print(e)




# placeholder