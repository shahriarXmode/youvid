from pytube import YouTube
import os

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return True, stream.default_filename
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)
    success, filename = download_youtube_video(url, output_path)
    if success:
        print(f"Video downloaded successfully as '{filename}' in '{output_path}' folder.")
    else:
        print("Failed to download video:", filename)

