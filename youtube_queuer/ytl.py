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


def ytl_add(args):
    data = {
            'url': args.url,
            'output_dir': args.output_dir
            }
    r = requests.post('http://localhost:1536/cli/add', json=data)
    r.raise_for_status()
    print('Queued')


def ytl_list(args):
    r = requests.get('http://localhost:1536/cli/list')
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
    r = requests.delete('http://localhost:1536/cli/delete', json=data)
    r.raise_for_status()
