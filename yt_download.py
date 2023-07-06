import yt_dlp
import os

def download_playlist(url, target_directory):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Define ytdl options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(target_directory, '%(title)s.%(ext)s'),
        'noplaylist': False,
        'ignoreerrors': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Define the URL of the playlist and the target directory
playlist_url = 'PLAYLIST URL'
target_directory = 'LOCAL DIRECTORY'

# Call the function
download_playlist(playlist_url, target_directory)