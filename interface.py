import controller_playlist
import pyinputplus

class Interface:
    def __init__(self) -> None:
        self.user_choice = None
        self.choices = {
            "1p": controller_playlist.create_playlist_controller,
            "2p": controller_playlist.remove_playlist_controller,
            "3p": controller_playlist.rename_playlist_controller,
            "4p": controller_playlist.add_songs_to_playlist_controller,
            "5p": controller_playlist.remove_songs_from_playlist_controller,
            "6p": controller_playlist.add_songs_from_existing_playlist_to_other_playlist_controller,
            "7p": controller_playlist.remove_all_songs_from_playlist_controller,
            "8p": controller_playlist.print_playlist_information_on_text_file_controller,
            "9p": controller_playlist.view_playlist_information_controller,
            "10p": controller_playlist.add_all_playlist_items_to_playlist_controller
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
        print("6p. Add a single playlist's song items to another playlist")
        print("7p. Remove all songs from playlist")
        print("8p. Send Playlist Songs To Markdown File")
        print("9p. View Playlist Information")
        print("10p. Add all playlist song items to one playlist")
    
    def print_quit(self):
        print("q. Quit program")  # added option to quit

    def get_choice(self):
        self.user_choice = pyinputplus.inputStr(prompt="your choice -> ")

    def handleChoice(self):
        if "p" in self.user_choice:
            self.handlePlaylistChoice()
        elif "q" == self.user_choice:
            print("Exiting program...")
            exit()
        else:
            print("Invalid choice : try again...")
            self.user_choice = None

       

    def handlePlaylistChoice(self):
        if self.user_choice in self.choices:
            self.choices[self.user_choice]()
        