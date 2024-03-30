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

             