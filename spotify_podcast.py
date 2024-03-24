import os
import spotipy
import requests
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyPodcast:
    def __init__(self, client_id, client_secret, output_folder):
        print(f'client_id: {client_id}')
        print(f'client_secret: {client_secret}')
        
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
        self.output_folder = output_folder
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def download_episode(self, podcast_url):
        # Parse the podcast ID from the URL
        parsed_url = urllib.parse.urlparse(podcast_url)
        podcast_id = parsed_url.path.split("/")[-1]
        print(f'Podcast ID: {podcast_id}')
        
        # Retrieve the podcast data using the Spotify API
        episode = self.sp.episode(podcast_id, market="US")

        # Download the audio file
        audio_url = episode["audio_preview_url"]
        response = requests.get(audio_url)
        # Save the file in the specified output folder
        filename = os.path.join(self.output_folder, f"{podcast_id}.mp3")
        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Episode downloaded: {filename}")
        
        return filename
