from __future__ import print_function, division, absolute_import
import requests
import os
from youtube_queuer.logs import create_logger


logger = create_logger('youtube_queuer.ytq')


def main(args):
    if args.cmd == 'add':
        ytq_add(args)
    elif args.cmd == 'list':
        ytq_list(args)
    elif args.cmd == 'delete':
        ytq_delete(args)
    else:
        raise NotImplementedError('Command not implemented: {}'.format(args.cmd))


def get_root_url(args):
    logger.debug('Getting root url with args %s', args)
    return 'http://{host}:{port}'.format(
            host=args.host, port=args.port)


def ytq_add(args):
    logger.info('Adding video: %s -> %s', args.url, args.output_dir)
    data = {
            'url': args.url,
            'output_dir': args.output_dir
            }
    root_url = get_root_url(args)
    logger.debug('Sending web request')
    r = requests.post('{}/cli/add'.format(root_url), json=data)
    r.raise_for_status()
    logger.info('Queued')


def ytq_list(args):
    logger.info('Listing queued videos')
    root_url = get_root_url(args)
    r = requests.get('{}/cli/list'.format(root_url))
    r.raise_for_status()
    content = r.json()

    if not len(content):
        print('No queued items found')
    else:
        for item in content:
            print('{} "{}" {}'.format(item['id'], item['title'], item['added']))


def ytq_delete(args):
    video_id = args.id
    logger.info('Deleting video %s', video_id)
    data = {
            'video_id': video_id,
            }
    root_url = get_root_url(args)
    r = requests.delete('{}/cli/delete'.format(root_url), json=data)
    r.raise_for_status()
