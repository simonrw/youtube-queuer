import argparse
import youtube_queuer.ytld


def ytld_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', required=False, default=1536)
    parser.add_argument('-H', '--host', required=False, default='127.0.0.1')
    ytld.main(parser.parse_args())

