"""
File: service_playlist.py
Description: Controller module responsible for managing user interactions and API connections related to playlists.
@author: Michael-Andre Odusami
@version: March 2024
"""

import backend_utility
from backend_playlist import add_playlist_songs_to_playlist

def add_songs_from_existing_playlist_to_other_playlist(destination_playlist_name, source_playlist_name):
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
        playlist_to_add_to_id = backend_utility.get_playlist_id(destination_playlist_name)
        source_playlist_id = backend_utility.get_playlist_id(source_playlist_name)
        
        # Add songs to the destination playlist
        add_playlist_songs_to_playlist(playlist_id=playlist_to_add_to_id, source_playlist_id=source_playlist_id)
    
    except Exception as e:
        print(e)




# placeholder