from aiohttp import web
import json

# Temporary
users = []

async def register(request):
    data = await request.post()
    try:
        username = data['username']
        email = data['email']
        password = data['password']
    except KeyError as e:
        return web.json_response({"error": "email already exists"}, status=200)

    # Invalid form entries
    if (username == "") or (email == "") or (password == ""):
        return web.json_response({"error": "email already exists"}, status=200)

    # Check if user already exists (by using email and username)
    for user in users:
        if user["email"] == email:
            return web.json_response({"error": "email already exists"}, status=200)

    # If user doesn't already exist, send success
    users.append({"email": email, "username": username, "password": password})
    return web.json_response({"msg": "success"}, status=200)

async def login(request):
    data = await request.post()
    try:
        password = data['password']
        email = data['email']
    except KeyError as e:
        return web.json_response({"error": "invalid credentials"}, status=200)

    # Invalid form entries
    if (email == "") or (password == ""):
        return web.json_response({"error": "invalid credentials"}, status=200)

    # Check if user exists in database
    for user in users:
        if user["email"] == email and user["password"] == password:
            return web.json_response({"msg": "success"}, status=200)

    # If we are here, the user doesn't exist
    return web.json_response({"error": "invalid email/password"}, status=200)
