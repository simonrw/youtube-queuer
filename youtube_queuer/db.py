import os
import sqlite3

def db_init(filename):

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
        os.remove(filename)
    except OSError:
        pass

    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        for stmt in statements:
            cur.execute(stmt)

