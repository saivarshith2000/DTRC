from aiohttp import web
import json

async def commit(request):
    db = request.app['db']
    cmd = await request.post()
    print(cmd)
    return web.Response(text="OK")

