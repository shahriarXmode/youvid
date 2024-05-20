from pytube import YouTube
import os
import http.server
import socketserver
import webbrowser

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return True, stream.default_filename
    except Exception as e:
        return False, str(e)

def serve_video(filename):
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving video at http://localhost:{PORT}")
        webbrowser.open_new_tab(f"http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)
    success, filename = download_youtube_video(url, output_path)
    if success:
        print(f"Video downloaded successfully as '{filename}' in '{output_path}' folder.")
        serve_video(os.path.join(output_path, filename))
    else:
        print("Failed to download video:", filename)
