# Podcast Transcription Tool

This repository contains a tool designed to transcribe podcast episodes. Utilizing the power of Hugging Face's `distilwhisper` model, the tool breaks down audio files into manageable chunks and transcribes them, offering an accessible way to convert spoken content into written form.

## Features

- **Podcast Downloading**: Downloads podcast episodes from Spotify.
- **Audio Chunking**: Splits large audio files into smaller chunks for efficient processing.
- **Transcription**: Transcribes audio content using the `distilwhisper` model from Hugging Face's Transformers library.
- **Progress Tracking**: Includes a progress bar for real-time transcription status updates.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- `pip` for installing Python packages

### Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/belgrano9/podcast_transcriber.git
   ```
2. **Install Required Libraries**

   Navigate to the cloned repository's directory and install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

   This command installs all necessary dependencies, including `transformers`, `tqdm`, `pydub`, and `python-dotenv`.

### Usage

1. **Environment Variables**

   Set up your `.env` file in the project's root directory with your API keys and other configurations. Example:

   ```
   SPOTIFY_CLIENT_KEY=your_key_here
   SPOTIFY_SECRET_KEY=your_key_here
   ```
2. **Transcribing a Podcast Episode**

   Use the `run_transcription.py` script to transcribe a podcast episode. Specify the path to the audio file as an argument:

   ```bash
   python run_transcription.py "path/to/your/podcast/episode.mp3"
   ```

   The script will output the transcription to a text file in the same directory as the audio file.

## Contributing

Contributions are welcome! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter)

Project Link: [https://github.com/belgrano9/podcast_transcriber](https://github.com/belgrano9/podcast_transcriber)

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the Transformers library and the `distilwhisper` model.
- [Spotify](https://www.spotify.com/) for the podcast content.
