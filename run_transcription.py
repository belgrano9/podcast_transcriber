from transcribe_podcast import HuggingFaceTranscriber

# Initialize the transcriber
transcriber = HuggingFaceTranscriber()

# Specify the path to your audio file
audio_path = r"C:\Users\tomso\workspace\podcast_transcriber\downloads\1RB4AvszL2hhAXXiOVNGXz.mp3"

# Run the transcription process
transcription = transcriber.transcribe(audio_path)

# Optionally, print the full transcription to the console
print("Transcription:\n", transcription)
