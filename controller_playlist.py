"""
File: controller_playlist.py
This file is responsible for handling playlist interactions with the user
@author: Michael-Andre Odusami
@version: March 2024
"""
import pyinputplus as pyip
import service_playlist

def prompt_user(self, prompt):
    """
    Prompt the user

    Parameters:
    - prompt (str): The prompt message to display to the user.

    Returns:
    - str: The answer to the prompt
    """
    response = pyip.inputStr(prompt)
    return response

def add_songs_from_existing_playlist_to_other_playlist_controller(self):
    destination_playlist_name = self.prompt_user("Enter the name of the destination playlist: ")
    source_playlist_name = self.prompt_user("Enter the name of the source playlist: ")
    response = service_playlist.add_songs_from_existing_playlist_to_other_playlist_service(destination_playlist_name=destination_playlist_name, source_playlist_name=source_playlist_name)
    print(response)

def create_playlist_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to create: ")
    description_of_playlist = self.prompt_user("Enter the description of the playlist: ")
    response = service_playlist.create_playlist_service(title=name_of_playlist, description=description_of_playlist)
    print(response)

def remove_playlist_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to remove: ")
    response = service_playlist.remove_playlist_service(title=name_of_playlist)
    print(response)

def rename_playlist_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to rename: ")
    new_name_of_playlist = self.prompt_user("Enter the new name of the playlist: ")
    response = service_playlist.rename_playlist_service(title=name_of_playlist, newTitle=new_name_of_playlist)
    print(response)

def add_songs_to_playlist_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to add to: ")
    songs = []
    while True:
        song = self.prompt_user("Enter the name of the song you want to add | Enter -1 to stop: ")
        if song == "-1":
            break
        songs.append(song)
    response = service_playlist.add_songs_to_playlist_service(title=name_of_playlist, song_names=songs)
    print(response)


def remove_songs_from_playlist_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to remove a song from: ")
    songs = []
    while True:
        song = self.prompt_user("Enter the name of the song you want to remove | Enter -1 to stop: ")
        if song == "-1":
            break
        songs.append(song)
    response = service_playlist.remove_songs_from_playlist_service(title=name_of_playlist, song_names=songs)
    print(response)

def remove_all_songs_from_playlist_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to remove a song from: ")
    confirmation = (pyip.inputYesNo(prompt="Are you sure you want to remove all songs from playlist (Yes or No): ")).lower()
    if confirmation == "yes" or confirmation == "y":
        response = service_playlist.remove_all_songs_from_playlist_service(title=name_of_playlist)
        print(response)
    else:
        print("[FAILED] Removing all songs from playlist")

def print_playlist_information_on_text_file_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to be displayed on the file: ")
    name_of_textfile = self.prompt_user("Enter the title of the text file to be created: ")
    print(service_playlist.print_playlist_information_on_text_file_service(title=name_of_playlist, file_name=name_of_textfile))

def view_playlist_information_controller(self):
    name_of_playlist = self.prompt_user("Enter the name of the playlist to be displayed: ")
    objects = service_playlist.get_playlist_information(title=name_of_playlist)
    if not isinstance(objects, list):
        print(objects)
        return

    print("\nGeneral Information:")
    for key, value in objects[0].items():
        print(f"{key}: {value}")

    # Printing out the tracks information
    print("\nTracks Information:")
    for index, track in enumerate(objects[1], start=1):
        print(f"Track {index}:")
        for key, value in track.items():
            print(f"  {key}: {value}")