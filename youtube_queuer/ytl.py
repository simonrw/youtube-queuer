import requests


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
    pass


def ytl_list(args):
    r = requests.get('http://localhost:1536/cli/list')
    r.raise_for_status()
    content = r.json()

    if not len(content):
        print('No queued items found')

    for i, item in enumerate(content):
        print('{} "{}"'.format(i + 1, item))


def ytl_stop(args):
    pass
