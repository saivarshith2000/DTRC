from aiohttp import web
import json
import sqlite3
import aiohttp

# Adds a user to the database. Returns True if success, False otherwise
async def add_user(db, replicas, username, email, password):
    cmd = f"insert into User values ('{username}','{email}','{password}');"
    print(cmd)
    try:
        cursor = db.cursor()
        cursor.execute(cmd)
        db.commit()
    except Exception as e:
        print(str(e))
        # If this failed, it means there is already a user with the same email
        return False
    # Now send command to other replicas, if atleast one disagrees -> abort
    session = aiohttp.ClientSession()
    accepted = []
    for replica in replicas:
        try:
            resp = await session.post(replica + "/cmd", json={'cmd': cmd})
            result = await resp.text()
            if (result == "OK"):
                accepted.append(replica)
            else:
                print(f"server {replica} did not accept {cmd}")
                continue
        except Exception as e:
            print(f"server {replica} did not respond to {cmd}")
    
    # If even one server did not accept, rollback
    if len(accepted) != len(replicas):
        # rollback the last commit
        db.rollback()
        # send rollback calls to other replicas
        for replica in accepted:
            try:
                resp = await session.post(replica + "/cmd", json={"cmd": "rollback"})
            except Exception as e:
                print(f"server {replica} did not rollback -> inconsistency !!!")
        await session.close()
    else:
        await session.close()
        return True

# Check if a user exists in database. Returns email if true, None otherwise
def check_user(db, email, password):
    # No need to contact replicas for READS !!!
    cursor = db.cursor()
    row = cursor.execute(f"SELECT username FROM User WHERE email LIKE '{email}' AND password LIKE '{password}'").fetchone()
    if row is None:
        return None
    else:
        return row['username']

async def register(request):
    db = request.app['db']
    replicas = request.app['replicas']
    data = await request.post()
    try:
        username = data['username']
        email = data['email']
        password = data['password']
    except KeyError as e:
        return web.json_response({"error": "invalid form"}, status=200)

    # Invalid form entries
    if (username == "") or (email == "") or (password == ""):
        return web.json_response({"error": "invalid form"}, status=200)

    success = await add_user(db, replicas, username, email, password)
    if success:
        return web.json_response({"msg": "success"}, status=200)
    # failure
    return web.json_response({"error": "registration error"}, status=200)


async def login(request):
    db = request.app['db']
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
    username = check_user(db, email, password) 
    if username:
        return web.json_response({"msg": "success", "email": email, "username": username}, status=200)

    # If we are here, the user doesn't exist
    return web.json_response({"error": "invalid email/password"}, status=200)
