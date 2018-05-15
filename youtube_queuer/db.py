import os
import sqlite3
from youtube_queuer.logs import create_logger, set_verbosity


logger = create_logger('youtube_queuer.db')


def db_init(filename):

    logger.info('Initialising database')

    statements = ['''CREATE TABLE yt_queue (
        id integer primary key,
        title string not null,
        url string not null unique,
        output_dir string not null,
        start integer,
        end integer,
        added timestamp not null default current_timestamp
        );
        ''', '''INSERT INTO yt_queue (title, url, output_dir) VALUES (
            'SOMEBODY TOUCHA MY SPAGHET',
            'https://www.youtube.com/watch?v=cE1FrqheQNI', '/tmp');
    ''']

    try:
        os.remove(filename)
    except OSError:
        logger.debug('No database file to remove')
        pass

    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        for stmt in statements:
            logger.debug('Executing statement:\n%s', stmt)
            cur.execute(stmt)

