from __future__ import print_function, division, absolute_import
import argparse
import youtube_queuer.ytld
import youtube_queuer.ytl
import youtube_queuer.ytl_worker


def ytld_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536, type=int)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    ytld.main(parser.parse_args())


def ytl_main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('url')
    parser_add.add_argument('-o', '--output-dir', required=True)

    parser_list = subparsers.add_parser('list')

    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('id', type=int)

    ytl.main(parser.parse_args())


def ytl_worker_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536, type=int)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    parser.add_argument('-s', '--sleep-time', required=False, default=10, type=int)
    ytl_worker.main(parser.parse_args())


def db_init():
    import os
    import sqlite3

    statements = ['''
    CREATE TABLE yt_queue (
        id integer primary key,
        title string not null,
        url string not null unique,
        output_dir string not null,
        added timestamp not null default current_timestamp
        );
        ''', '''INSERT INTO yt_queue (title, url, output_dir) VALUES (
            'SOMEBODY TOUCHA MY SPAGHET',
            'https://www.youtube.com/watch?v=cE1FrqheQNI', '/tmp');
    ''']

    try:
        os.remove('db.db')
    except FileNotFoundError:
        pass

    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        for stmt in statements:
            cur.execute(stmt)
