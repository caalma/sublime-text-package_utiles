#!/usr/bin/python3
# -*- coding:utf8 -*- 

# ref : https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312

from sys import argv
from youtube_dl import YoutubeDL

def yt_info(url, clave):
    ydl_opts = {
        'quiet': True,
        'verbose': False,
    }
    with YoutubeDL(ydl_opts) as ydl:
        d = ydl.extract_info(url, download=False)
        return d[clave]
    return ''

if __name__ == '__main__':
    r = yt_info(argv[1], argv[2])
    print(r)
    exit()

# comando bash para usar con lista
# for l in $(cat l); do echo "$l # "$(python3 ./yt_info.py "$l" title) >> l_ct;done