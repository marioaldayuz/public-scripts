import openai
import os

openai.api_key = "YOUR_API_KEY_HERE"

input_directory = input("Enter the path to your input directory: ").strip()
user_prompt = input("Enter your prompt for rewriting the text: ").strip()
output_directory = input("Enter the path to your output directory: ").strip()

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: {output_directory}")

# Iterate through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):  # Check if the file is a text file
        input_file_path = os.path.join(input_directory, filename)
        try:
            with open(input_file_path, 'r', encoding='utf-8') as file:
                input_text = file.read()

            response = openai.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": user_prompt},
                    {"role": "user", "content": input_text},
                ],
                temperature=0.3,
                max_tokens=4096
            )

            rewritten_text = response.choices[0].message.content if response.choices else "No response generated."

            # Generate a title using a second OpenAI completion
            title_prompt = "Create a file name containing key elements and words for the previous response with no extension. The title should be no longer than 90 characters and includ a brief synopsis or keyword based phrase related to the content. It should be written at an 8th grade level and not include words like guide or maximize."
            title_response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": title_prompt},
                    {"role": "user", "content": rewritten_text},
                ],
                temperature=0.2,
                max_tokens=100
            )

            generated_title = title_response.choices[0].message.content if title_response.choices else "untitled"
            sanitized_filename = "".join([c if c.isalnum() else "_" for c in generated_title])[:100]  # Sanitize and limit to 100 characters
            output_file_path = os.path.join(output_directory, f"{sanitized_filename}.txt")

            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(rewritten_text)

            print(f"Rewritten text written to: {output_file_path}")
        except Exception as e:
            print(f"An error occurred with file {filename}: {e}")
            continue  # Continue to the next file even if an error occurs
