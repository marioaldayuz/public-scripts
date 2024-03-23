import time
from vimeo_downloader import Vimeo

embedded_on = 'https://EMBEDDED_WEBSITE/'

def read_video_info(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    return [line for line in lines if line]

def download_video_with_backoff(line, max_retries=5):
    title, video_id = line.split(',', 1)  # Split on the first comma only
    retry_count = 0
    wait_time = 35  # Initial wait time of 5 seconds

    while retry_count < max_retries:
        try:
            v = Vimeo.from_video_id(video_id, embedded_on=embedded_on)
            # Check if streams are available
            if v.streams:
                filename = ''.join([c if c.isalnum() or c in " ._-()" else "_" for c in line])
                v.streams[0].download(download_directory='video', filename=filename)
                print(f"Downloaded: {filename}")
                return  # Exit the function upon successful download
            else:
                print(f"No streams available for video {title} ({video_id})")
                return
        except Exception as e:
            print(f"An error occurred while processing video {title} ({video_id}): {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            wait_time *= 2  # Double the wait time for the next retry
            retry_count += 1

    print(f"Failed to download video {title} ({video_id}) after {max_retries} retries.")

video_lines = read_video_info('YOUR_TEXT_FILE.txt')

for line in video_lines:
    download_video_with_backoff(line)
    time.sleep(10)  # Wait for 5 seconds before moving to the next video
