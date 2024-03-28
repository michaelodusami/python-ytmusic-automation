"""
this file is responsible for handling playlist interactions with the user
@author: Michael-Andre Odusami
@version: March 2024
"""
import pyinputplus as pyip
import service_playlist


class Playlist:
        def __init__(self) -> None:
            pass

        def get_playlist_name(self, prompt):
            """
            Prompt the user to enter the name of a playlist.

            Parameters:
            - prompt (str): The prompt message to display to the user.

            Returns:
            - str: The name of the playlist entered by the user.
            """
            playlist_name = pyip.inputStr(prompt)
            return playlist_name

        def add_songs_from_existing_playlist_to_other_playlist(self):
            destination_playlist_name = self.get_playlist_name("Enter the name of the destination playlist: ")
            source_playlist_name = self.get_playlist_name("Enter the name of the source playlist: ")
            service_playlist.add_songs_from_existing_playlist_to_other_playlist(destination_playlist_name=destination_playlist_name, source_playlist_name=source_playlist_name)




myP = Playlist()
myP.add_songs_from_existing_playlist_to_other_playlist()