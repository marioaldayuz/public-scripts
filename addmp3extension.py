import os

# Specify the directory containing the files
directory = 'youtube'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Construct the full file path
    old_file = os.path.join(directory, filename)
    # Check if the file does not have an extension
    if os.path.isfile(old_file) and '.' not in filename:
        # Construct the new file name with the .mp3 extension
        new_file = f"{old_file}.mp3"
        # Rename the file
        os.rename(old_file, new_file)

print("All applicable files have been renamed with the .mp3 extension.")
