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
    info = fetch_next(host=host, port=port)
    if info is None:
        return

    download(url=info['url'])
    mark_as_complete(host=host, port=port, video_id=info['video_id'])


def fetch_next(host, port):
    url = 'http://{host}:{port}/worker/next'.format(
            host=host, port=port)
    r = requests.get(url)
    r.raise_for_status()
    j = r.json()
    if j['status_code'] == 0:
        return j
    elif j['status_code'] == 1:
        logger.info('No new videos')
        return None
    else:
        raise RuntimeError('An error occurred')


def download(url):
    logger.info('Downloading using url %s', url)
    yt.download(url)


def mark_as_complete(host, port, video_id):
    data = {'video_id': video_id}
    url = 'http://{host}:{port}/worker/complete'.format(
            host=host, port=port)
    r = requests.post(url, json=data)
    r.raise_for_status()
