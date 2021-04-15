from aiohttp import web
from pprint import pprint

from auth import login, register
from ticket import get_tickets, book_ticket

# server config
PORT = 8001

def main(port=PORT):
    app = web.Application()
    # Auth routes
    app.add_routes([web.post('/register', register)])
    app.add_routes([web.post('/login', login)])
    # Ticket routes
    app.add_routes([web.get('/tickets', get_tickets)])
    app.add_routes([web.post('/book', book_ticket)])
    # start server
    print(f"Started DRTC server on port: {PORT}")
    web.run_app(app, port=port)

if __name__ == "__main__":
    main()
