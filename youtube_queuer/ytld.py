from flask import Flask, jsonify
import sqlite3


app = Flask('ytld')


@app.route('/worker/next')
def next():
    return jsonify({})


def main(args):
    app.run(debug=True, port=args.port, host=args.host)
