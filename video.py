from pytube import YouTube
import os

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        video_file_path = os.path.join(save_path, yt.title + '.mp4')
        stream.download(output_path=video_file_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def main():
    video_url = input("Enter the YouTube video URL: ")
    save_path = "/home/shahriarmahmudoune150/youvid/video"  # Absolute path to the video folder

    download_video(video_url, save_path)

if __name__ == "__main__":
    main()
