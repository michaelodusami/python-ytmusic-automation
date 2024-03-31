from controller_playlist import Playlist
import pyinputplus

class Interface:
    def __init__(self) -> None:
        self.playlistController = Playlist()
        self.user_choice = None
        self.choices = {
            "1p": self.playlistController.create_playlist_controller,
            "2p": self.playlistController.remove_playlist_controller,
            "3p": self.playlistController.rename_playlist_controller,
            "4p": self.playlistController.add_songs_to_playlist_controller,
            "5p": self.playlistController.remove_songs_from_playlist_controller,
            "6p": self.playlistController.add_songs_from_existing_playlist_to_other_playlist_controller,
            "7p": self.playlistController.remove_all_songs_from_playlist_controller,
            "8p": self.playlistController.print_playlist_information_on_text_file_controller,
        }

    def print_title(self, title):
         print(f"\n======= {title} =======")
    
    def playlist_menu(self):
        self.print_title("Playlist Options")
        print("1p. Create a new playlist")
        print("2p. Remove a playlist")
        print("3p. Rename a playlist")
        print("4p. Add a song to a playlist")
        print("5p. Remove a song from a playlist")
        print("6p. Add all playlist song items to another playlist")
        print("7p. Remove all songs from playlist")
        print("8p. Send Playlist Songs To Markdown File")

    def get_choice(self):
        self.user_choice = pyinputplus.inputStr(prompt="your choice -> ")

    def handleChoice(self):
        if "p" in self.user_choice:
            self.handlePlaylistChoice()
        # reset choice
        self.user_choice = None

    def handlePlaylistChoice(self):
        if self.user_choice in self.choices:
            self.choices[self.user_choice]()
        