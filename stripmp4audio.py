import subprocess
import os
import time

def convert_mp4_to_mp3_with_retries(source_folder, target_folder=None, audio_format='mp3', max_retries=5):
    """
    Converts all MP4 files in the source_folder to the specified audio_format with retries and saves them in the target_folder.

    Args:
    source_folder (str): The path to the folder containing MP4 files.
    target_folder (str): The path to the folder where the converted audio files will be saved. If None, uses source_folder.
    audio_format (str): The target audio format (default is 'mp3').
    max_retries (int): Maximum number of retries for converting each file.
    """
    if target_folder is None:
        target_folder = source_folder

    # Ensure target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # List all MP4 files in the source folder
    mp4_files = [f for f in os.listdir(source_folder) if f.endswith('.mp4')]

    for mp4_file in mp4_files:
        attempt = 1
        retry_delay = 2  # Initial retry delay in seconds
        while attempt <= max_retries:
            full_mp4_path = os.path.join(source_folder, mp4_file)
            audio_file_name = f"{os.path.splitext(mp4_file)[0]}.{audio_format}"
            full_audio_path = os.path.join(target_folder, audio_file_name)

            # Construct and execute the ffmpeg command
            cmd = ['ffmpeg', '-i', full_mp4_path, '-vn', '-ab', '128k', '-ar', '44100', '-y', full_audio_path]
            try:
                subprocess.run(cmd, check=True)
                print(f"Converted {mp4_file} to {audio_file_name}")
                break  # Exit loop after successful conversion
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {mp4_file} on attempt {attempt}: {e}")
                if attempt < max_retries:
                    time.sleep(retry_delay)  # Wait before retrying
                    retry_delay *= 2  # Exponential backoff
                attempt += 1
        if attempt > max_retries:
            print(f"Failed to convert {mp4_file} after {max_retries} attempts.")

# Example usage
if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    target_folder = input("Enter the target folder path (leave blank to use the same as source folder): ")
    target_folder = target_folder if target_folder else None
    convert_mp4_to_mp3_with_retries(source_folder, target_folder)
