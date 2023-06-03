# install pip install youtube_dl package

import youtube_dl
url = input("Enter the URL of  youtube Video: \n ")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])
