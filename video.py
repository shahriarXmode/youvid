from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "/home/shahriarmahmudoune150/youvid/video"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=DOWNLOAD_FOLDER)
        return redirect(url_for('videos'))
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/videos')
def videos():
    video_files = os.listdir(DOWNLOAD_FOLDER)
    return render_template('videos.html', videos=video_files)

@app.route('/video/<filename>')
def video(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)
