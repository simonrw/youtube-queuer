from aiohttp import web
import aioodbc


routes = web.RouteTableDef()


class WebHandler(object):
    def __init__(self):
        pass

    def worker_next(self, request):
        return web.Response(text='Hello world')


def main(args):
    app = web.Application()
    handler = WebHandler()
    app.add_routes([web.get('/worker/next', handler.worker_next)])
    web.run_app(app, host=args.host, port=args.port)
