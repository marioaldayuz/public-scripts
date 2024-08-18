import os
from bs4 import BeautifulSoup

def html_to_text(html_content):
    """Convert HTML content to plain text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def convert_folder_to_text(source_folder, output_folder):
    """Convert all HTML files in a folder to text files."""
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".html"):
            file_path = os.path.join(source_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                text = html_to_text(html_content)
            
            # Write the text to a new file in the output folder
            output_file_path = os.path.join(output_folder, filename.replace('.html', '.txt'))
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            print(f'Converted {filename} to text.')

if __name__ == "__main__":
    source_folder = 'D:\\ExtendlyKBWL\\'
    output_folder = 'D:\\ExtendlyKBWL\\text\\'
    convert_folder_to_text(source_folder, output_folder)
