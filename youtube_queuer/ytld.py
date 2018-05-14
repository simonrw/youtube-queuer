from aiohttp import web


def main(args):
    app = web.Application()
    web.run_app(app, host=args.host, port=args.port)
