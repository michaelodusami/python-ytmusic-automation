from ytmusic_instance import my_ytmusic
import utility


# users are able to add all existing playlist songs to an exisitng playlist or new playlist
"""
Will need to: 
- YTMusic.add_playlist_items(playlistId: str, videoIds: List[str] | None = None, source_playlist: str | None = None, duplicates: bool = False)→ str | Dict
    - will need the playlist id of the song to add to
    - will need a list of video id's to add to this playlist
    - or the source playlist to add songs to
"""

def add_playlist_songs_to_playlist(playlist_id : str, source_playlist_id: str, duplicates = False):
    my_ytmusic.add_playlist_items(playlistId=playlist_id, source_playlist=source_playlist_id, duplicates=bool)


try:
    playlist_to_add_to_id = utility.get_playlist_id("songs");
    source_playlist_id = utility.get_playlist_id("rap");
    add_playlist_songs_to_playlist(playlist_id=playlist_to_add_to_id, source_playlist_id=source_playlist_id)
except Exception as e:
    print(e)
