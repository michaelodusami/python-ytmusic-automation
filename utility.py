from ytmusic_instance import my_ytmusic




"""
to use in a try catch block
Gets the playlist id of a playlist depending on the name
"""
def get_playlist_id(name_of_playlist: str):
    playlists = my_ytmusic.get_library_playlists();

    my_playlist_id = None
    for playlist in playlists:
        if name_of_playlist.lower() == playlist["title"].lower():
            print(f"Playlist {name_of_playlist.upper()} found...\n")
            # print(playlist)
            my_playlist_id = playlist["playlistId"];
    
    if my_playlist_id == None:
       raise Exception("Playlist not found") 
    
    return my_playlist_id


