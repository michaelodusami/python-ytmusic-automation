"""
File: controller_playlist.py
This file is responsible for handling playlist interactions with the user
@author: Michael-Andre Odusami
@version: March 2024
"""
import pyinputplus as pyip
import service_playlist


class Playlist:
        def __init__(self) -> None:
            pass

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

        def add_songs_from_existing_playlist_to_other_playlist(self):
            destination_playlist_name = self.prompt_user("Enter the name of the destination playlist: ")
            source_playlist_name = self.prompt_user("Enter the name of the source playlist: ")
            service_playlist.add_songs_from_existing_playlist_to_other_playlist_service(destination_playlist_name=destination_playlist_name, source_playlist_name=source_playlist_name)

        def create_playlist_controller(self):
            name_of_playlist = self.prompt_user("Enter the name of the playlist to create: ")
            description_of_playlist = self.prompt_user("Enter the description of the playlist: ")
            service_playlist.create_playlist_service(title=name_of_playlist, description=description_of_playlist)

        def remove_playlist_controller(self):
            name_of_playlist = self.prompt_user("Enter the name of the playlist to remove: ")
            service_playlist.remove_playlist_service(title=name_of_playlist)
        
        def rename_playlist_controller(self):
            name_of_playlist = self.prompt_user("Enter the name of the playlist to rename: ")
            new_name_of_playlist = self.prompt_user("Enter the new name of the playlist: ")
            service_playlist.rename_playlist_service(title=name_of_playlist, newTitle=new_name_of_playlist)
        
        def add_songs_to_playlist(self):
            name_of_playlist = self.prompt_user("Enter the name of the playlist to add to: ")
            songs = []
            while True:
                song = self.prompt_user("Enter the name of the song you want to add | Enter -1 to stop: ")
                if song == "-1":
                    break
                songs.append(song)
            service_playlist.add_songs_to_playlist_service(title=name_of_playlist, song_names=songs)