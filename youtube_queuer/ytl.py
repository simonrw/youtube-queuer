from __future__ import print_function, division, absolute_import
import requests
import os


def main(args):
    if args.cmd == 'add':
        ytl_add(args)
    elif args.cmd == 'list':
        ytl_list(args)
    elif args.cmd == 'delete':
        ytl_delete(args)
    else:
        raise NotImplementedError('Command not implemented: {}'.format(args.cmd))


def get_root_url(args):
    return 'http://{host}:{port}'.format(
            host=args.host, port=args.port)


def ytl_add(args):
    data = {
            'url': args.url,
            'output_dir': args.output_dir
            }
    root_url = get_root_url(args)
    r = requests.post('{}/cli/add'.format(root_url), json=data)
    r.raise_for_status()
    print('Queued')


def ytl_list(args):
    root_url = get_root_url(args)
    r = requests.get('{}/cli/list'.format(root_url))
    r.raise_for_status()
    content = r.json()

    if not len(content):
        print('No queued items found')

    for item in content:
        print('{} "{}" {}'.format(item['id'], item['title'], item['added']))


def ytl_delete(args):
    video_id = args.id
    data = {
            'video_id': video_id,
            }
    root_url = get_root_url(args)
    r = requests.delete('{}/cli/delete'.format(root_url), json=data)
    r.raise_for_status()
