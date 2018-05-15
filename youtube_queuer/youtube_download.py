from __future__ import print_function, division, absolute_import
import youtube_dl
from youtube_queuer.logs import create_logger


logger = create_logger('youtube_queuer.youtube_download')


def find_title(url):
    logger.info('Finding title for %s', url)
    opts = {
            'playliststart': 1,
            'playlistend': 1,
            }
    with youtube_dl.YoutubeDL(opts) as ydl:
        logger.debug('Extracting info from youtube API')
        info = ydl.extract_info(url, download=False)

    return info['title']


def download(url):
    logger.info('Downloading video from %s', url)
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl.download([url])
