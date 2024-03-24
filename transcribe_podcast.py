import os
from dotenv import load_dotenv
from transformers import pipeline
from pydub import AudioSegment
from tqdm import tqdm  

class HuggingFaceTranscriber:
    def __init__(self):
        load_dotenv()
        # Initialize the transcription pipeline with the distilwhisper model
        self.transcriber = pipeline(model="distil-whisper/distil-large-v3", task="automatic-speech-recognition")

    def chunk(self, audio_path):
        file_name = os.path.basename(audio_path)
        file_size = os.path.getsize(audio_path)
        audio_list = []

        # Get length of audio file
        audio = AudioSegment.from_mp3(audio_path)
        duration = len(audio) / 1000  # Duration in seconds
        print(f'↪ Processing file: {file_name} ({duration / 60:.2f} minutes)')

        if file_size > 25 * 1024 * 1024:
            print(f'↪ The audio file is too large: {(file_size / 1024 / 1024):.2f} MB (>25MB), chunking...')
            # The directory to save chunks
            chunk_dir = f"downloads/hf/{file_name.split('.')[0]}"
            os.makedirs(chunk_dir, exist_ok=True)

            # PyDub handles time in milliseconds, chunk duration set to ~25 minutes
            chunk_length = 25 * 60 * 1000

            for i, chunk in enumerate(audio[::chunk_length]):
                chunk_name = os.path.join(chunk_dir, f"{file_name.split('.')[0]}_{i}.mp3")
                if not os.path.exists(chunk_name):
                    chunk.export(chunk_name, format="mp3")
                audio_list.append(chunk_name)
        else:
            audio_list.append(audio_path)
            
        return audio_list

    def transcribe(self, audio_path):
        print(f'🗣️  Initializing transcription...')

        audio_list = self.chunk(audio_path)
        print(f'↪ Chunk size: {len(audio_list)}')

        transcriptions = []

        # Wrap audio_list with tqdm for a progress bar
        for audio in tqdm(audio_list, desc="Transcribing Chunks"):
            print(f'\t↪ Transcribing {audio}...')
            transcript_path = f"{audio.split('.')[0]}.txt"
            
            if not os.path.exists(transcript_path):
                # Transcribe the audio file
                result = self.transcriber(audio)
                transcript = result["text"]

                # Save the transcript to a text file
                with open(transcript_path, "w") as f:
                    f.write(transcript)
                
                print(f"\t\t↪ Saved transcript to {transcript_path}")
            else:
                # Load an existing transcript
                with open(transcript_path, "r") as f:
                    transcript = f.read()
            
            transcriptions.append(transcript)

        full_transcript = ' '.join(transcriptions)
        print(f'↪ Total words: {len(full_transcript.split())}')
        return full_transcript
