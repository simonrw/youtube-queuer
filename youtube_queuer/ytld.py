from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/worker/next')
async def worker_next(request):
    return web.Response(text='Hello world')


def main(args):
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=args.host, port=args.port)
