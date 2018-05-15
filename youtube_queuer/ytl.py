import requests
import os


def main(args):
    if args.cmd == 'add':
        ytl_add(args)
    elif args.cmd == 'list':
        ytl_list(args)
    elif args.cmd == 'stop':
        ytl_stop(args)
    else:
        raise NotImplementedError('Command not implemented: {}'.format(args.cmd))


def ytl_add(args):
    cmd = args.args
    output_dir = os.path.realpath(args.output_dir)

    data = {
            'args': cmd,
            'output_dir': output_dir,
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


def ytl_stop(args):
    pass
