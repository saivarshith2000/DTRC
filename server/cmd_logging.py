from aiohttp import web
import json

async def append(request):
    return web.Response(text="OK")

