from ytmusic_instance import my_ytmusic
import backend_utility


def add_playlist_songs_to_playlist(playlist_id : str, source_playlist_id: str):
    my_ytmusic.add_playlist_items(playlistId=playlist_id, source_playlist=source_playlist_id, duplicates=True)


