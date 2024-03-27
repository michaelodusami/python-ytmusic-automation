import utility
from Playlist import add_playlist_songs_to_playlist

def add_songs_from_existing_playlist_to_other_playlist():
    try:
        playlist_to_add_to_id = utility.get_playlist_id("songs");
        source_playlist_id = utility.get_playlist_id("rap");
        add_playlist_songs_to_playlist(playlist_id=playlist_to_add_to_id, source_playlist_id=source_playlist_id)
    except Exception as e:
        print(e)

