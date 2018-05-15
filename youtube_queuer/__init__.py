from __future__ import print_function, division, absolute_import
import argparse
import youtube_queuer.ytqd
import youtube_queuer.ytq
import youtube_queuer.ytq_worker
from youtube_queuer.db import db_init


def ytqd_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536, type=int)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    parser.add_argument('--debug', required=False, default=False, action='store_true')
    ytqd.main(parser.parse_args())


def ytq_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536, type=int)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')

    subparsers = parser.add_subparsers(dest='cmd')

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('url')
    parser_add.add_argument('-o', '--output-dir', required=True)

    parser_list = subparsers.add_parser('list')

    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('id', type=int)

    ytq.main(parser.parse_args())


def ytq_worker_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536, type=int)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    parser.add_argument('-s', '--sleep-time', required=False, default=10, type=int)
    ytq_worker.main(parser.parse_args())
