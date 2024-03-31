"""
File: service_playlist.py
Description: Controller module responsible for managing user interactions and API connections related to playlists.
@author: Michael-Andre Odusami
@version: March 2024
"""

import backend_playlist 
import Levenshtein
import pprint

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

def create_playlist_service(title = "New Playlist", description = ""):
    backend_playlist.create_playlist(title=title,description=description)

def remove_playlist_service(title : str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        backend_playlist.delete_playlist(playlist_id)
    except Exception as e:
        print(e)

def rename_playlist_service(title : str, newTitle : str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        backend_playlist.rename_playlist(playlist_id=playlist_id, title=newTitle)
    except Exception as e:
        print(e)

def add_songs_to_playlist_service(title : str, song_names: list):
    try:
        song_ids = []
        for song in song_names:
            data = backend_playlist.get_song_information(song)
            song_ids.append(data["videoId"])

        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        tracks = backend_playlist.get_playlist_tracks(playlist_id=playlist_id)
        # make sure the songs to be added does not already exists
            # get a list of song ids in that playlist and skip over the ids that are in the set
        # add that list of ids to the playlist
        track_song_ids = list(set([track["videoId"] for track in tracks]))
        unique_song_ids = [song_id for song_id in song_ids if song_id not in track_song_ids]
        if not unique_song_ids:
            print("Songs already in playlist.")
            return
        backend_playlist.add_playlist_songs_to_playlist_with_list_of_video_id(playlist_id=playlist_id, list_of_songs=unique_song_ids)
    except Exception as e:
        print(e)
    
def remove_songs_from_playlist_service(title: str, song_names: list):
    def is_similar(word1, word2, threshold=2):
        distance = Levenshtein.distance(word1, word2)
        return distance <= threshold
    def filter_similar_tracks(tracks, song_names, threshold=2):
        similar_tracks = []
        for track in tracks:
            for song_name in song_names:
                if is_similar(track["title"], song_name, threshold):
                    similar_tracks.append(track)
                    break  # Break the inner loop once a similar track is found
        return similar_tracks
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        videos = backend_playlist.get_playlist(playlist_id=playlist_id)
        playlist_tracks = videos["tracks"]
        similar_tracks = filter_similar_tracks(playlist_tracks, song_names)
        if not similar_tracks:
            print("Song not found.")
            return
        backend_playlist.remove_song_from_playlist(playlist_id=playlist_id, songs=similar_tracks)
        
    except Exception as e:
        print(e)

def remove_all_songs_from_playlist_service(title: str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        tracks = backend_playlist.get_playlist_tracks(playlist_id=playlist_id)
        backend_playlist.remove_song_from_playlist(playlist_id=playlist_id, songs=tracks)
    except Exception as e:
        print(e)