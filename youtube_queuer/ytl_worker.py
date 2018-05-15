import argparse
import time
import requests
import youtube_queuer.youtube_download as yt
from youtube_queuer.logs import create_logger


logger = create_logger('ytl-worker')


def main(args):
    while True:
        try:
            loop_step(host=args.host, port=args.port)
        except Exception as e:
            logger.exception('Unhandled exception')

        logger.debug('Sleeping for %s seconds', args.sleep_time)
        time.sleep(args.sleep_time)


def loop_step(host, port):
    logger.debug('Taking loop step')

    logger.info('Checking for latest video')
    url = fetch_next(host=host, port=port)
    download(url=url)


def fetch_next(host, port):
    url = 'http://{host}:{port}/worker/next'.format(
            host=host, port=port)
    r = requests.get(url)
    r.raise_for_status()
    j = r.json()
    if j['status_code'] != 0:
        raise RuntimeError('Failed to get next video')

    url = j['url']
    return url


def download(url):
    logger.info('Downloading using url %s', url)
    yt.download(url)
