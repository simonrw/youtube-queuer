from aiohttp import web


async def worker_next(request):
    return web.Response(text='Hello world')


def main(args):
    app = web.Application()
    app.add_routes([
        web.get('/worker/next', worker_next),
        ])
    web.run_app(app, host=args.host, port=args.port)
