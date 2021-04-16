import asyncio
import aiohttp
from aiohttp import web
from pprint import pprint
import sys
import requests
import sqlite3

from auth import login, register
from ticket import get_tickets, book_ticket
from cmd import commit

# server config
rp_addr = "http://0.0.0.0:8000"
PORT = 8001
is_primary = False
#replicas = ["http://0.0.0.0:8002", "http://0.0.0.0:8003", "http://0.0.0.0:8001"] 
replicas = ["http://0.0.0.0:8002", "http://0.0.0.0:8001"] 

# temporary function to create auth table
def create_tables(db):
    db.execute("create table if not exists User(username varchar(30) not null, email varchar(30) not null unique, password varchar(30) not null);")
    db.commit()
    print("created tables")


def main():
    global is_primary
    global replicas
    port = PORT
    if (len(sys.argv) > 1):
        port = int(sys.argv[1])
    if (port < 8001) or (port > 8003):
        print("Invalid port number. port number ranges from 8001 to 8003")
        return

    # Check if database is accessible
    try :
        db = sqlite3.connect(f'{port}.db')
        db.row_factory = sqlite3.Row
        print("database access successful")
        # create_tables(db)
    except Exception as e:
        print(str(e))
        return

    # address of self
    addr = f"http://0.0.0.0:{port}"
    # remove self from list of replicas
    replicas.remove(addr)
    print(replicas)
    # ask the reverse proxy to set self as leader
    try:
        resp = requests.get(f"{rp_addr}/setleader", params = {"addr": addr}).json()
        primary = resp['primary']
        if primary == addr:
            is_primary = True
    except Exception as e:
        print(f"The reverse proxy server {rp_addr} can't be reached. please try again later")
        return

    app = web.Application()
    # Auth routes
    app.add_routes([web.post('/register', register)])
    app.add_routes([web.post('/login', login)])
    # Ticket routes
    app.add_routes([web.post('/tickets', get_tickets)])
    app.add_routes([web.post('/book', book_ticket)])
    # Command log
    app.add_routes([web.post('/cmd', commit)])
    # add database connection to the app instance
    app['db'] = db
    app['replicas'] = replicas

    # start server
    if (is_primary):
        print(f"Started PRIMARY DRTC server on port: {port}")
    else:
        print(f"Started REPLICA DRTC server on port: {port}")
    web.run_app(app, port=port)
    db.close()

if __name__ == "__main__":
    main()
