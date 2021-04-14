import aiohttp
from aiohttp import web

# auth routes - forward client request to auth service
AUTH_REGISTER_URL = "http://0.0.0.0:8081/register"
AUTH_LOGIN_URL = "http://0.0.0.0:8081/login"

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
        return web.Response(status=500, text="service down")

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
        return web.Response(status=500, text="service down")

# Forward get ticket request to ticket primary

# Forward book ticket request to ticket primary

def main():
    app = web.Application()
    # Routes
    app.add_routes([web.post('/auth/login', auth_login)])
    app.add_routes([web.post('/auth/register', auth_register)])
    print("Started REVERSE PROXY")
    web.run_app(app, port=8080)

if __name__ == "__main__":
    main()
