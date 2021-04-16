from aiohttp import web
import json

async def commit(request):
    db = request.app['db']
    data = await request.json()
    cmd = data["cmd"]
    # If primary sends a rollback message, rollback the current transaction
    if (cmd == "rollback"):
        db.rollback()
        return web.Response(text="OK")
    print(cmd)
    cursor = db.cursor()
    # Try to execute the cmd, if it fails, return ABORT to the primary, then the commit will be cancelled
    try:
        cursor.execute(cmd)
        db.commit()
        return web.Response(text="OK")
    except Exception as e:
        print(str(e))
        return web.Response(text="ABORT")
