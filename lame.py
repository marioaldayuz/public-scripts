import os
import subprocess

def compress_mp3_files(source_directory, compressed_subdirectory, quality, resample_rate):
    # Full path to the compressed files directory
    compressed_directory = os.path.join(source_directory, compressed_subdirectory)

    # Create the subdirectory if it doesn't exist
    if not os.path.exists(compressed_directory):
        os.makedirs(compressed_directory)

    # Loop through all files in the source directory
    for filename in os.listdir(source_directory):
        if filename.endswith(".mp3"):
            # Construct the full file paths
            source_file = os.path.join(source_directory, filename)
            compressed_file = os.path.join(compressed_directory, f"compressed_{filename}")

            # Compress the file using LAME with specified quality and resample rate
            try:
                subprocess.run(["lame", f"-V{quality} --resample {resample_rate}", source_file, compressed_file], check=True)
                print(f"Successfully compressed: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error compressing file {filename}: {e}")

    print("Compression completed. Compressed files are in the 'compressed' subfolder.")

if __name__ == "__main__":
    # Prompt the user for necessary information
    source_directory = input("Enter the source directory containing the MP3 files: ")
    compressed_subdirectory = input("Enter the name for the subdirectory to store compressed files: ")
    quality = input("Enter the desired quality level (0-9, where 0 is highest quality and 9 is lowest): ")
    resample_rate = input("Enter the desired resample rate in kHz (e.g., 16 for 16kHz): ")

    # Validate user input where necessary (basic validation)
    try:
        quality = int(quality)
        assert 0 <= quality <= 9
        resample_rate = float(resample_rate)
        assert resample_rate > 0
    except (ValueError, AssertionError):
        print("Invalid quality or resample rate entered. Please enter valid numbers.")
    else:
        compress_mp3_files(source_directory, compressed_subdirectory, quality, resample_rate)
