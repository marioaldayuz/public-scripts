from pytube import Playlist
import os

def download_playlist(playlist_url, output_dir, audio_only=False):
    playlist = Playlist(playlist_url)
    print(f"Downloading playlist: {playlist.title}")

    for video in playlist.videos:
        print(f"Downloading video: {video.title}")
        if audio_only:
            # Download the audio stream with the highest bitrate
            audio_stream = video.streams.get_audio_only()
            audio_stream.download(output_path=output_dir)
        else:
            # Download the highest resolution video
            video_stream = video.streams.get_highest_resolution()
            video_stream.download(output_path=output_dir)
    print("Download completed.")

if __name__ == "__main__":
    # Ask for user input
    playlist_url = input("Enter the playlist URL: ")
    output_dir = input("Enter the output directory: ")
    audio_only_input = input("Do you want to download audio only? (yes/no): ")

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine if the user wants audio only
    audio_only = audio_only_input.strip().lower() == 'yes'

    # Download the playlist
    download_playlist(playlist_url, output_dir, audio_only)

