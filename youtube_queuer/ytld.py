from flask import Flask, jsonify, request
import sqlite3
import subprocess as sp
import re
import youtube_queuer.youtube_download as yt


URL_MATCHER = re.compile(r'https?://.*\.?youtube\.com[^\'"]+')


app = Flask('ytld')


@app.route('/worker/next')
def next():
    with sqlite3.connect('db.db') as c:
        cur = c.cursor()
        cur.execute('''select arguments from yt_queue
        order by added desc
        limit 1''')
        rows = cur.fetchone()
        if rows:
            args = {
                    'status': 'ok',
                    'status_code': 0,
                    'arguments': rows[0],
                    }
        else:
            args = {
                    'status': 'no-results',
                    'status_code': 1,
                    }
        return jsonify(args)


@app.route('/cli/list')
def list_queued():
    with sqlite3.connect('db.db') as c:
        cur = c.cursor()
        cur.execute('''select id, title, added from yt_queue
        order by added asc''')
        rows = cur.fetchall()
        return jsonify([{'id': row[0], 'title': row[1], 'added': row[2]} for row in rows])


@app.route('/cli/add', methods=['POST'])
def add_item():
    req = request.json
    url = extract_url(req['args'])
    title = find_title(url)
    with sqlite3.connect('db.db') as c:
        cur = c.cursor()
        cur.execute('''insert into yt_queue (title, arguments, output_dir) values
        (?, ?, ?)''', (title, req['args'], req['output_dir']))
    return 'ok'


def extract_url(args):
    words = args.split()
    for word in words:
        match = URL_MATCHER.search(word)
        if match:
            return match.group(0)
    raise ValueError('No url found in arguments')


def find_title(url):
    return yt.find_title(url)



def main(args):
    app.run(debug=True, port=args.port, host=args.host)
