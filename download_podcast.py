from spotify_podcast import SpotifyPodcast
import os
from dotenv import load_dotenv

# Load API credentials from .env file
load_dotenv()

CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")

# Specify the output folder where you want to save the podcast episodes
OUTPUT_FOLDER = 'podcast_transcriber/downloads/'

# Initialize the SpotifyPodcast object with your credentials and output folder
spotify_podcast = SpotifyPodcast(CLIENT_ID, CLIENT_SECRET, OUTPUT_FOLDER)

# The URL of the podcast episode you want to download
PODCAST_URL = 'https://open.spotify.com/episode/1RB4AvszL2hhAXXiOVNGXz'

# Use the download_episode method to download the podcast
filename = spotify_podcast.download_episode(PODCAST_URL)

print(f"Downloaded episode file: {filename}")
