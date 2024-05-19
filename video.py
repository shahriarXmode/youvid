from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def main():
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path to save the video: ")

    download_video(video_url, save_path)

if __name__ == "__main__":
    main()
