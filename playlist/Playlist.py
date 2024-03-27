

# users are able to add all existing playlist songs to an exisitng playlist or new playlist
"""
Will need to: 
- YTMusic.add_playlist_items(playlistId: str, videoIds: List[str] | None = None, source_playlist: str | None = None, duplicates: bool = False)→ str | Dict
    - will need the playlist id of the song to add to
    - will need a list of video id's to add to this playlist
    - or the source playlist to add songs to
"""

def add_playlist_songs_to_playlist(playlist_id : str, source_playlist: str):
    