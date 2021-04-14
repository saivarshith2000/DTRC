from aiohttp import web
from pprint import pprint

# server config
PORT = 8003

# Handle get tickets request
async def get_tickets(request):
    params = request.query
    print(params)
    # Get ticket information - from, to, date
    return web.Response(status=200, text="OK")

# Handle book ticket request
async def book_ticket(request):
    # Get ticket information - from, to, date, train
    return web.Response(status=200, text="OK")


def main(port=PORT):
    app = web.Application()
    app.add_routes([web.get('/tickets', get_tickets)])
    app.add_routes([web.post('/book', book_ticket)])
    print("Started AUTH Service")
    web.run_app(app, port=port)

if __name__ == '__main__':
    main()
