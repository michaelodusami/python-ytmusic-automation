"""
This script initializes a YTMusic object using the YTMusicAPI library.

YTMusicAPI allows for interacting with YouTube Music's web interface,
including searching for songs, playlists, albums, artists, and managing
user library, playlist, and metadata.

Make sure to replace "oauth.json" with the path to your OAuth credentials file.

For more information about YTMusicAPI, visit: https://ytmusicapi.readthedocs.io/en/stable/usage.html
"""

# Importing necessary library
from ytmusicapi import YTMusic

# Initialize a YTMusic object using OAuth credentials from "oauth.json"
my_ytmusic = YTMusic("oauth.json")
