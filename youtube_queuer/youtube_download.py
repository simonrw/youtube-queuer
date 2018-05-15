import youtube_dl


def find_title(url):
    opts = {
            'playliststart': 1,
            'playlistend': 1,
            }
    with youtube_dl.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return info['title']


def download(url):
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl.download([url])
