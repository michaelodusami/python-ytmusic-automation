"""
File: service_playlist.py
Description: Controller module responsible for managing user interactions and API connections related to playlists.
@author: Michael-Andre Odusami
@version: March 2024
"""

import backend_playlist 
import Levenshtein
import pprint
import json

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
            return "Songs already in playlist..."
        return backend_playlist.add_playlist_songs_to_playlist_with_list_of_video_id(playlist_id=destination_playlist_id, list_of_songs=unique_songs)
    except Exception as e:
        return e

def create_playlist_service(title = "New Playlist", description = ""):
   return backend_playlist.create_playlist(title=title,description=description)

def remove_playlist_service(title : str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        return backend_playlist.delete_playlist(playlist_id)
    except Exception as e:
        return e

def rename_playlist_service(title : str, newTitle : str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        return backend_playlist.rename_playlist(playlist_id=playlist_id, title=newTitle)
    except Exception as e:
        return e

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
            return "Songs already in playlist."
        return backend_playlist.add_playlist_songs_to_playlist_with_list_of_video_id(playlist_id=playlist_id, list_of_songs=unique_song_ids)
    except Exception as e:
        return e
    
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
            return "Song not found."
        return backend_playlist.remove_song_from_playlist(playlist_id=playlist_id, songs=similar_tracks)
        
    except Exception as e:
        return e

def remove_all_songs_from_playlist_service(title: str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        tracks = backend_playlist.get_playlist_tracks(playlist_id=playlist_id)
        return backend_playlist.remove_song_from_playlist(playlist_id=playlist_id, songs=tracks)
    except Exception as e:
        return e

def print_playlist_information_on_text_file_service(title: str, file_name: str):
    def write_attribute(file, obj, attribute_name):
        if attribute_name in obj:
            value = obj[attribute_name]
            if isinstance(value, dict):
                if 'name' in value and 'id' in value:
                    file.write(f"  - **{attribute_name.capitalize()}**: {value['name']} (ID: {value['id']})\n")
                else:
                    file.write(f"  - **{attribute_name.capitalize()}**: {value}\n")
            elif isinstance(value, list):
                file.write(f"  - **{attribute_name.capitalize()}**: ")
                for item in value:
                    if isinstance(item, dict) and 'name' in item and 'id' in item:
                        file.write(f"{item['name']} (ID: {item['id']}), ")
                    else:
                        file.write(f"{item}, ")
                file.write("\n")
            else:
                file.write(f"  - **{attribute_name.capitalize()}**: {value}\n")
        else:
            file.write(f"  - **{attribute_name.capitalize()}**: N/A\n")
    def write_object_to_file(obj, file_name):
        with open(file_name + ".md", 'w') as file:
            # Write file name
            file.write(f"# {file_name}\n\n")
            
            # Write attributes of obj
            file.write("## General:\n")
            attributes_to_write = ['id', 'privacy', 'title', 'description', 'author', 'duration', 'duration_seconds', 'trackCount']
            for attribute in attributes_to_write:
                write_attribute(file, obj, attribute)
            file.write("\n")

            # Write Tracks
            file.write("## Tracks:\n")
            for track in obj['tracks']:
                file.write(f"### Track: {track['title']}\n")
                attributes_to_write = ['title', 'videoId', 'artists', 'album', 'likeStatus', 'isAvailable', 'isExplicit', 'videoType']
                for attribute in attributes_to_write:
                    write_attribute(file, track, attribute)
                file.write("\n")

    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        obj = backend_playlist.get_playlist(playlist_id=playlist_id)
        write_object_to_file(obj=obj, file_name=file_name)
        return f"Text File - {file_name} - Created"
    except Exception as e:
        return e

def get_playlist_information(title: str):
    try:
        playlist_id = backend_playlist.get_playlist_id(name_of_playlist=title)
        playlist = backend_playlist.get_playlist(playlist_id=playlist_id)
        backup_value = "N/A"
        if not playlist:
            return "error"
        general_info = {
            "id": playlist.get("id", backup_value),
            "title": playlist.get("title", backup_value),
            "description": playlist.get("description", backup_value),
            "year": playlist.get("year", backup_value),
            "author": playlist.get("author", backup_value),
            "total duration": playlist.get("duration", backup_value),
            "total trackCount": playlist.get("trackCount", backup_value)
        }

        return general_info
    except Exception as e:
        return e