from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    save_path = "video"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    video_file_path = os.path.join(save_path, yt.title + '.mp4')
    stream.download(output_path=video_file_path)
    return f"Download completed! Video saved as: {video_file_path}"

if __name__ == '__main__':
    app.run(debug=True)
