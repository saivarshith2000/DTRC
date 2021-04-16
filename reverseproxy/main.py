import aiohttp
from aiohttp import web
import sys

# reverseproxy config
PORT = 8000
primary = None
replicas = ["http://0.0.0.0:8001", "http://0.0.0.0:8002", "http://0.0.0.0:8003"]

# Forward register request to auth primary
async def auth_register(request):
    if primary == None:
        return web.Response(status=500, text="auth service down")
    register_url = primary + "/register"
    session = aiohttp.ClientSession()
    body = await request.post()
    try:
        resp = await session.post(register_url, data=body)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception as e:
        await session.close()
        return web.Response(status=500, text="auth service down")

# Forward login request to auth primary
async def auth_login(request):
    if primary == None:
        return web.Response(status=500, text="auth service down")
    login_url = primary + "/login"
    session = aiohttp.ClientSession()
    body = await request.post()
    try:
        resp = await session.post(login_url, data=body)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        await session.close()
        return web.Response(status=500, text="auth service down")

# Forward get ticket request to ticket primary
async def get_tickets(request):
    if primary == None:
        return web.Response(status=500, text="ticket service down")
    get_tick_url = primary + "/tickets"
    session = aiohttp.ClientSession()
    data = await request.json()
    try:
        resp = await session.post(get_tick_url, json=data)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        await session.close()
        return web.Response(status=500, text="ticket service down")


# Forward book ticket request to ticket primary
async def book_ticket(request):
    if primary == None:
        return web.Response(status=500, text="ticket service down")
    book_ticket_url = primary + "/tickets"
    session = aiohttp.ClientSession()
    body = await request.post()
    try:
        resp = await session.post(book_ticket_url, data=body)
        result = await resp.text()
        await session.close()
        return web.Response(body=result, status=resp.status, headers=resp.headers)
    except Exception:
        await session.close()
        return web.Response(status=500, text="ticket service down")

# Set leader
# every replica asks the reverseproxy to make it the primary on startup. The replica that asked first becomes the primary.
# If a primary already exists, then the address of the leader is returned
async def setleader(request):
    global primary
    global replicas
    params = request.query
    # add replica details to replica list
    replica = params['addr']
    if primary is None:
        # If a primary is not yet selected, select the node that sent this request as primary and remove it from list of replicas
        primary = replica
        replicas.remove(primary)
        print(f"primary update to {primary}")
    else:
        # If a primary already exists, send the address of primary
        replicas.append(replica)
    return web.json_response({"primary": primary})

# App thread
def main():
    port = PORT
    if (len(sys.argv) > 1):
        port = int(sys.argv[1])
    app = web.Application()
    # Routes
    app.add_routes([web.get('/setleader', setleader)])
    app.add_routes([web.post('/login', auth_login)])
    app.add_routes([web.post('/register', auth_register)])
    app.add_routes([web.post('/tickets', get_tickets)])
    app.add_routes([web.post('/book', book_ticket)])
    print("Replicas: ")
    for replica in replicas:
        print(f"{replica}")
    print("-------------------------")
    print(f"Started REVERSE PROXY on port: {port}")
    web.run_app(app, port=port)

if __name__ == "__main__":
    main()
