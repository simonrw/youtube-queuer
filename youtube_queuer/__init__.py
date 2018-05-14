import argparse
import youtube_queuer.ytld


def ytld_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    ytld.main(parser.parse_args())


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


    

