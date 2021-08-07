
from __future__ import unicode_literals
import youtube_dl
ydl_opts = {'format': 'best','external-downloader':'aria2c','outtmpl':'javid.mp4'}  #using aria2c as external downloader massively speeds up download
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                      ydl.download(['https://www.youtube.com/watch?v=Z--lECtqAuM'])