import os
import pypandoc

def get_user_input():
    # Ask for the HTML file path
    html_file_path = input("Enter the path to your HTML file: ")
    if not os.path.exists(html_file_path):
        print("The specified HTML file does not exist. Exiting...")
        return None, None
    
    # Ask for the output directory path
    output_dir = input("Enter the path where you want to output the DOCX file: ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output folder: {output_dir}")

    # Generate the output DOCX file path
    docx_file_name = os.path.splitext(os.path.basename(html_file_path))[0] + ".docx"
    docx_file_path = os.path.join(output_dir, docx_file_name)

    return html_file_path, docx_file_path

def convert_html_to_docx(html_file_path, docx_file_path):
    try:
        # Automatically download Pandoc if it is not installed
        pypandoc.download_pandoc()

        # Convert the HTML file to DOCX using pypandoc
        pypandoc.convert_file(html_file_path, 'docx', format='html', outputfile=docx_file_path)
        print(f"Successfully created: {docx_file_path}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def main():
    html_file_path, docx_file_path = get_user_input()
    if html_file_path and docx_file_path:
        convert_html_to_docx(html_file_path, docx_file_path)

if __name__ == "__main__":
    main()
