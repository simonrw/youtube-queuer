from flask import Flask, jsonify, request, render_template
import sqlite3
import subprocess as sp
import re
import youtube_queuer.youtube_download as yt


URL_MATCHER = re.compile(r'https?://.*\.?youtube\.com[^\'"]+')


app = Flask('ytld')


@app.route('/worker/next')
def next():
    with sqlite3.connect('db.db') as c:
        try:
            cur = c.cursor()
            cur.execute('''select id, url, output_dir from yt_queue
            order by added asc
            limit 1''')
            row = cur.fetchone()
            if row:
                args = {
                        'status': 'ok',
                        'status_code': 0,
                        'video_id': row[0],
                        'url': row[1],
                        'output_dir': row[2],
                        }
            else:
                args = {
                        'status': 'no-results',
                        'status_code': 1,
                        }
        except sqlite3.Error:
            args = {
                    'status': 'database-error',
                    'status_code': 2,
                    }
        return jsonify(args)


@app.route('/worker/complete', methods=['POST'])
def mark_as_complete():
    video_id = request.json['video_id']
    delete_queued_item(video_id)
    return jsonify({'status': 'ok'})


@app.route('/cli/list')
def list_queued():
    entries = list_entries()
    return jsonify([{'id': entry[0], 'title': entry[1], 'added': entry[2]} for entry in entries])


@app.route('/cli/add', methods=['POST'])
def add_item():
    req = request.json
    url = req['url']
    title = find_title(url)
    with sqlite3.connect('db.db') as c:
        cur = c.cursor()
        try:
            cur.execute('''insert into yt_queue (title, url, output_dir) values (?, ?, ?)''',
                    (title, url, req['output_dir']))
        except sqlite3.IntegrityError:
            pass

    return jsonify({'status': 'ok'})


@app.route('/cli/delete', methods=['DELETE'])
def delete_item():
    req = request.json
    video_id = req['video_id']

    delete_queued_item(video_id)

    return jsonify({'status': 'ok'})


@app.route('/')
def index():
    items = list_entries()
    return render_template('index.html', items=items)


def delete_queued_item(video_id):
    with sqlite3.connect('db.db') as c:
        cur = c.cursor()
        cur.execute('''delete from yt_queue where id = ?''', (video_id,))


def extract_url(args):
    words = args.split()
    for word in words:
        match = URL_MATCHER.search(word)
        if match:
            return match.group(0)
    raise ValueError('No url found in arguments')


def find_title(url):
    return yt.find_title(url)


def list_entries():
    with sqlite3.connect('db.db') as c:
        cur = c.cursor()
        cur.execute('''select id, title, added from yt_queue
        order by added asc''')
        rows = cur.fetchall()

    return rows

def main(args):
    app.run(debug=True, port=args.port, host=args.host)
