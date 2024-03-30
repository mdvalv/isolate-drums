import sys
from yt_dlp import YoutubeDL
from spleeter.separator import Separator

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Usage: python main.py <url>")
        exit(1)

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'outtmpl': 'songs/%(title)s.%(ext)s',
    }

    URLS = [url]
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URLS[0], download=False)
        if info is None:
            print("Failed to download video.", file=sys.stderr)
            exit(1)
        title = info['title']
        ydl.download(URLS)

    separator = Separator('spleeter:5stems')
    input_audio_path = f'songs/{title}.m4a'
    output_directory = 'output'
    separator.separate_to_file(input_audio_path, output_directory)
