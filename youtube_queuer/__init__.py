import argparse
import youtube_queuer.ytld
import youtube_queuer.ytl


def ytld_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    ytld.main(parser.parse_args())


def ytl_main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('-a', '--args', required=True)
    parser_add.add_argument('-o', '--output-dir', required=True)

    parser_list = subparsers.add_parser('list')

    parser_stop = subparsers.add_parser('stop')
    parser_stop.add_argument('id')

    ytl.main(parser.parse_args())


def db_init():
    import os
    import sqlite3

    statements = ['''
    CREATE TABLE yt_queue (
        id integer primary key,
        arguments string not null,
        added timestamp not null default current_timestamp
        );
        ''', '''INSERT INTO yt_queue (arguments) VALUES (
            'https://www.youtube.com/watch?v=3-HMkXmJLO0');
    ''']

    try:
        os.remove('db.db')
    except FileNotFoundError:
        pass

    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        for stmt in statements:
            cur.execute(stmt)
