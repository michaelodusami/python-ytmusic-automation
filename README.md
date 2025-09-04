# YouTube Music Playlist Manager

## TL;DR (Overview)
The **YouTube Music Playlist Manager** is a Python command-line tool for managing YouTube Music playlists. Built with the `ytmusicapi` library, it allows users to create, delete, rename, and modify playlists, add or remove songs, and export playlist details to markdown files. Its modular design separates backend API interactions, service logic, and user interface, offering a streamlined experience for playlist automation.

## Skills Demonstrated
- **Programming Language**: Python
- **Libraries/Frameworks**: `ytmusicapi` for YouTube Music API integration, `pyinputplus` for input validation, `Levenshtein` for fuzzy string matching
- **API Interaction**: OAuth authentication, handling playlist and song API requests
- **Software Architecture**: Separation of concerns with backend, service, controller, and interface layers
- **Error Handling**: Comprehensive exception handling for robust API and user input management
- **File I/O**: Generating markdown files for playlist data export
- **Data Processing**: Filtering unique songs, handling JSON data, and fuzzy matching for song titles
- **User Interface**: Menu-driven command-line interface
- **Development Tools**: VS Code debugging configuration (`launch.json`)
- **Version Control**: Project structured with `.gitignore` and Apache License 2.0

## Installation

### Prerequisites
- Python 3.x
- Install required dependencies:
  ```bash
  pip install ytmusicapi pyinputplus python-Levenshtein
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
3. Place the `oauth.json` file in the project root directory for use by `ytmusic_instance.py`. This step is handled automatically in the provided setup.

### Running the Program
Run the application with:
```bash
python main.py
```
A menu will display playlist management options. Enter the option code (e.g., `1p` to create a playlist) and follow the prompts. Enter `q` to exit.

## Functionality
The application supports:
- **Create a Playlist**: Add a new playlist with a custom title and description.
- **Remove a Playlist**: Delete a specified playlist.
- **Rename a Playlist**: Change the name of an existing playlist.
- **Add Songs to a Playlist**: Search and add songs by name, ensuring no duplicates.
- **Remove Songs from a Playlist**: Remove songs using fuzzy matching for titles.
- **Add Songs from One Playlist to Another**: Copy unique songs between playlists.
- **Remove All Songs from a Playlist**: Clear all tracks with confirmation.
- **Export Playlist Information to Markdown**: Save playlist details (e.g., title, tracks, duration) to a markdown file.
- **View Playlist Information**: Display playlist details (e.g., ID, track count) in the console.
- **Add All Songs to One Playlist**: Merge songs from all playlists into one, avoiding duplicates.
- **Delete Multiple Playlists**: Remove multiple playlists in a single session.

## Project Structure Overview
- **backend_playlist.py**: Manages direct API calls for playlist and song operations.
- **service_playlist.py**: Handles business logic, including unique song filtering and fuzzy matching.
- **controller_playlist.py**: Processes user inputs and connects the interface to the service layer.
- **interface.py**: Provides a command-line menu for user interaction.
- **ytmusic_instance.py**: Initializes the `YTMusic` object for API communication.
- **main.py**: Program entry point.

## Example
1. Run:
   ```bash
   python main.py
   ```
2. Select `4p` to add songs to a playlist.
3. Enter the playlist name (e.g., "Workout Hits") and song names (e.g., "Sweet Caroline").
4. Continue adding songs or enter `-1` to stop. Exit with `q`.

## Notes
- A stable internet connection is required for API interactions.
- Song searches return the top result; use precise song names for best results.
- Fuzzy matching for song removal uses a Levenshtein distance threshold of 2.
- Errors (e.g., missing playlists, invalid inputs) are handled with clear messages.

## API Reference
Details on `ytmusicapi`:  
[https://ytmusicapi.readthedocs.io/en/stable/](https://ytmusicapi.readthedocs.io/en/stable/)

## License
Copyright 2024 Michael-Andre Odusami

Licensed under the Apache License, Version 2.0:  
[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES. See the License for permissions and limitations.

## Contact
Contact Michael-Andre Odusami via GitHub for questions or contributions.
