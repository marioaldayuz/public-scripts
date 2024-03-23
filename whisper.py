import openai
import os
import time

# Initialize the OpenAI client with your API key
openai.api_key = 'YOUR-API-KEY-HERE'

def transcribe_audio_file_with_retries(audio_path, max_retries=5):
    attempt = 1
    retry_delay = 2  # Initial retry delay in seconds
    while attempt <= max_retries:
        try:
            # Open the audio file in binary read mode
            with open(audio_path, "rb") as audio_file:
                # Call the OpenAI API to transcribe the audio file
                transcription = openai.Audio.transcribe(
                    model="whisper-1", 
                    file=audio_file
                )
                # Extract the transcription text
                return transcription.get('text')
        except Exception as e:
            print(f"Error transcribing file {audio_path}: {e}. Attempt {attempt} of {max_retries}")
            if attempt < max_retries:
                time.sleep(retry_delay)  # Wait before retrying
                retry_delay *= 2  # Exponential backoff
            attempt += 1
    print(f"Failed to transcribe '{audio_path}' after {max_retries} attempts.")
    return None  # Return None if all retries fail

def transcribe_audio_files(audio_folder_path, text_folder_path):
    # Ensure the text output folder exists, if not, create it
    if not os.path.exists(text_folder_path):
        os.makedirs(text_folder_path)

    # Iterate over each file in the audio folder
    for filename in os.listdir(audio_folder_path):
        if filename.endswith(".mp3"):
            # Construct the full path to the current audio file
            audio_path = os.path.join(audio_folder_path, filename)

            # Attempt to transcribe the audio file with retries
            transcription_text = transcribe_audio_file_with_retries(audio_path)

            if transcription_text:
                # Construct the output filename (replace .mp3 with .txt)
                output_filename = filename.replace(".mp3", ".txt")
                output_path = os.path.join(text_folder_path, output_filename)

                # Write the transcription to a text file in the text folder
                with open(output_path, "w") as text_file:
                    text_file.write(transcription_text)

                print(f"Transcribed '{filename}' to '{output_filename}'")
            else:
                print(f"Failed to transcribe '{filename}' after maximum retry attempts.")

if __name__ == "__main__":
    # Prompt the user for the paths to the audio and text folders
    audio_folder_path = input("Enter the path to the audio folder: ")
    text_folder_path = input("Enter the path to the folder where transcribed text files will be saved: ")
    
    # Transcribe all audio files in the folder
    transcribe_audio_files(audio_folder_path, text_folder_path)
