from flask import Flask, jsonify
import sqlite3


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
        cur.execute('''select id, title from yt_queue
        order by added desc''')
        rows = cur.fetchall()
        return jsonify([{'id': row[0], 'title': row[1]} for row in rows])


def main(args):
    app.run(debug=True, port=args.port, host=args.host)
