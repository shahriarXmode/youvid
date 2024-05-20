from pytube import YouTube
import os
import http.server
import socketserver
import base64
import webbrowser

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return True, stream.default_filename
    except Exception as e:
        return False, str(e)

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.authenticate():
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="Restricted"')
            self.end_headers()
            return

        super().do_GET()

    def authenticate(self):
        auth_header = self.headers.get("Authorization")
        if auth_header:
            auth_type, auth_value = auth_header.split(" ", 1)
            if auth_type.lower() == "basic":
                decoded_value = base64.b64decode(auth_value).decode("utf-8")
                username, password = decoded_value.split(":", 1)
                return username == "username" and password == "password"
        return False

def serve_video(filename):
    PORT = 8000

    Handler = AuthHandler

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

