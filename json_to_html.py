import os
import json
import re

# Function to get user input for file paths and folders
def get_user_input():
    json_file_path = input("Enter the path to your JSON file: ")
    if not os.path.exists(json_file_path):
        print("The specified file does not exist. Exiting...")
        return None, None
    
    output_dir = input("Enter the path where you want to output the HTML files: ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output folder: {output_dir}")
    
    return json_file_path, output_dir

# Function to sanitize file names
def sanitize_filename(filename):
    # Remove or replace characters that are invalid in file names
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Function to read JSON data and create HTML files
def create_html_files(json_file_path, output_dir):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        # Sanitize the file name
        file_name = f"{sanitize_filename(item['Text'])}.html"
        file_path = os.path.join(output_dir, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(item['Field'])
            print(f"Created: {file_path}")

def main():
    json_file_path, output_dir = get_user_input()
    if json_file_path and output_dir:
        create_html_files(json_file_path, output_dir)
        print("All files have been created.")

if __name__ == "__main__":
    main()
