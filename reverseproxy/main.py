import aiohttp
from aiohttp import web

# server config
PORT = 8000

# auth routes - forward client request to auth service
AUTH_REGISTER_URL = "http://0.0.0.0:8002/register"
AUTH_LOGIN_URL = "http://0.0.0.0:8002/login"

# ticket service - forward client request to ticket service
GET_TICKETS_URL = "http://0.0.0.0:8003/tickets"
BOOK_TICKETS_URL = "http://0.0.0.0:8003/book"

# Forward register request to auth primary
async def auth_register(request):
    session = aiohttp.ClientSession()
    body = await request.post()
    try:
        resp = await session.post(AUTH_REGISTER_URL, data=body)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        return web.Response(status=500, text="auth service down")

# Forward login request to auth primary
async def auth_login(request):
    session = aiohttp.ClientSession()
    body = await request.post()
    try:
        resp = await session.post(AUTH_LOGIN_URL, data=body)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        return web.Response(status=500, text="auth service down")

# Forward get ticket request to ticket primary
async def get_tickets(request):
    session = aiohttp.ClientSession()
    params = request.query
    try:
        resp = await session.get(GET_TICKETS_URL, params=params)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        return web.Response(status=500, text="ticket service down")


# Forward book ticket request to ticket primary
async def book_ticket(request):
    session = aiohttp.ClientSession()
    body = await request.post()
    try:
        resp = await session.post(BOOK_TICKETS_URL, data=body)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        return web.Response(status=500, text="ticket service down")

def main(port=PORT):
    app = web.Application()
    # Routes
    app.add_routes([web.post('/auth/login', auth_login)])
    app.add_routes([web.post('/auth/register', auth_register)])
    app.add_routes([web.get('/tickets', get_tickets)])
    app.add_routes([web.post('/book', book_ticket)])
    print(f"Started REVERSE PROXY on port: {port}")
    web.run_app(app, port=port)

if __name__ == "__main__":
    main()
