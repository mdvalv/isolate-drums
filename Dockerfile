FROM python:3.9

COPY main.py main.py

RUN apt-get update && apt-get install -y ffmpeg
RUN pip install spleeter yt_dlp

ENTRYPOINT [ "python", "main.py" ]
