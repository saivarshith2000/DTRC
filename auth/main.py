from aiohttp import web
from pprint import pprint

# server config
PORT = 8002

# Temporary
users = []

async def register(request):
    data = await request.post()
    try:
        username = data['username']
        email = data['email']
        password = data['password']
    except KeyError as e:
        return web.Response(status=400, text="invalid credentials")
    # Invalid form entries
    if (username == "") or (email == "") or (password == ""):
        return web.Response(status=400, text="invalid credentials")
    # Check if user already exists (by using email and username)
    for user in users:
        if user["email"] == email:
            return web.Response(status=400, text="email already exists")
    # If user doesn't already exist, send success
    users.append({"email": email, "username": username, "password": password})
    return web.Response(status=200, text="OK")

async def login(request):
    data = await request.post()
    try:
        password = data['password']
        email = data['email']
    except KeyError as e:
        print(e)
        return web.Response(status=400, text="invalid credentials")
    # Invalid form entries
    if (email == "") or (password == ""):
        return web.Response(status=400, text="invalid credentials")
    # Check if user exists in database
    for user in users:
        if user["email"] == email and user["password"] == password:
            return web.Response(status=200, text="OK")
    # If we are here, the user doesn't exist
    return web.Response(status=400, text="invalid email/password")

def main(port=PORT):
    app = web.Application()
    app.add_routes([web.post('/register', register)])
    app.add_routes([web.post('/login', login)])
    print(f"Started AUTH Service on port: {PORT}")
    web.run_app(app, port=port)

if __name__ == '__main__':
    main()
