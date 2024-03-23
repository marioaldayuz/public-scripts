import os
import subprocess

# Specify the directory containing the MP3 files
source_directory = 'yourdirectory'
# Specify the directory where the converted files will be saved
output_directory = 'yourdirectory/audio'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".mp3"):
        # Construct the full file paths
        source_file = os.path.join(source_directory, filename)
        output_file = os.path.join(output_directory, filename)
        
        # Convert the file using FFmpeg
        subprocess.run([
            "ffmpeg",
            "-i", source_file,  # Input file
            "-acodec", "libmp3lame",  # Use the LAME MP3 encoder
            "-ab", "128k",  # Set the bitrate to 128 kbps
            output_file  # Output file
        ], check=True)

print("Conversion completed. Converted files are in the specified output directory.")
