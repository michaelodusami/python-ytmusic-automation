# Playlist Manager Interface

This repository contains a Python program for managing playlists. The program allows users to perform various operations on playlists such as creating a new playlist, removing a playlist, adding or removing songs from a playlist, and more.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install ytmusicapi
```

## Usage

The program utilizes the `ytmusicapi` library for interacting with YouTube Music. Further setup is required only if you want to access account data using authenticated requests.

### OAuth Authentication

The simplest way to authenticate is to use OAuth authentication. Follow these steps:

1. After installing `ytmusicapi`, run the following command:

```bash
ytmusicapi oauth
```

2. Follow the instructions provided. This will create an `oauth.json` file in the current directory.

3. You can pass this `oauth.json` file to the parameter located in ytmusic_instance for authentication but this should be done for you

### Running the Program

Once dependencies are installed and authentication is set up, you can run the program using the `main.py` script.

```bash
python main.py
```

## Functionality

The program offers the following playlist management functionalities:

- Creating a new playlist
- Removing an existing playlist
- Renaming a playlist
- Adding a song to a playlist
- Removing a song from a playlist
- Adding all songs from one playlist to another
- Removing all songs from a playlist
- Sending playlist songs to a Markdown file
- Viewing playlist information

## Structure

**interface.py**
    - This file defines the Interface class responsible for managing user interactions and displaying the menu for playlist operations. It utilizes the controller_playlist module to execute user-selected actions.

**service_playlist.py**
    - This module serves as a controller layer responsible for managing user interactions and API connections related to playlists. It contains functions that handle various playlist operations, such as creating playlists, adding songs, removing playlists, and more. Each function in this module communicates with the backend_playlist module to perform the necessary actions.

**controller_playlist.py**
    - This file contains functions that act as an intermediary between the user interface (interface.py) and the service layer (service_playlist.py). These functions prompt the user for input and call the corresponding service functions to execute playlist operations.

**ytmusic_instance.py**
    - This script initializes a YTMusic object using the YTMusicAPI library, allowing interaction with YouTube Music's web interface. 

**backend_playlist.py**
    - This module serves as the backend layer responsible for directly interacting with the YouTube Music instance or account. It contains functions that perform actions such as adding songs to playlists, retrieving playlist information, creating playlists, and more. These functions utilize the YTMusic object initialized in ytmusic_instance.py to communicate with YouTube Music.

## Usage Instructions

1. When the program is executed, it presents a menu of playlist options.
2. Enter the corresponding option number to perform the desired operation.
3. If necessary, follow the prompts to provide additional information (e.g., playlist name, song details).
4. To quit the program, enter 'q' at any time.

Feel free to explore and modify the code according to your requirements!

Happy playlist management! 🎵

API used: https://ytmusicapi.readthedocs.io/en/stable/index.html

## License

    Copyright 2024 Michael-Andre Odusami

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.


