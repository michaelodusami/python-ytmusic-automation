"""
File: service_playlist.py
Description: Controller module responsible for managing user interactions and API connections related to playlists.
@author: Michael-Andre Odusami
@version: March 2024
"""

import backend_playlist 

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
        destination_playlist_id = backend_playlist.get_playlist_id(destination_playlist_name)
        source_playlist_id = backend_playlist.get_playlist_id(source_playlist_name)
        unique_songs = backend_playlist.find_unique_songs_for_playlist(destination_id=destination_playlist_id, source_id=source_playlist_id)
        if not unique_songs:
            print("Songs already in playlist...")
            return
        backend_playlist.add_playlist_songs_to_playlist_with_list_of_video_id(playlist_id=destination_playlist_id, list_of_songs=unique_songs)

    except Exception as e:
        print(e)

def create_playlist_service(title = "New Playlist", description = "", privacy_status = "PRIVATE"):
    backend_playlist.create_playlist(title=title, privacy_status=privacy_status, description=description)
