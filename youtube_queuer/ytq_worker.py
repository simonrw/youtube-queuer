from __future__ import print_function, division, absolute_import
import argparse
import time
import requests
from contextlib import contextmanager
import os
import youtube_queuer.youtube_download as yt
from youtube_queuer.logs import create_logger, set_verbosity


logger = create_logger('ytq-worker')


@contextmanager
def change_dir(new_cwd):
    old_cwd = os.getcwd()
    try:
        logger.debug('Changing directory to %s', new_cwd)
        os.chdir(new_cwd)
        yield
    finally:
        os.chdir(old_cwd)


def main(args):
    set_verbosity(logger, args.verbose)
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

    download(url=info['url'], output_dir=info['output_dir'], start=info['start'], end=info['end'])
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


def download(url, output_dir, start, end):
    output_dir = os.path.realpath(output_dir)

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    with change_dir(output_dir):
        logger.info('Downloading using url %s', url)
        yt.download(url, start=start, end=end)


def mark_as_complete(host, port, video_id):
    data = {'video_id': video_id}
    url = 'http://{host}:{port}/worker/complete'.format(
            host=host, port=port)
    r = requests.post(url, json=data)
    r.raise_for_status()
