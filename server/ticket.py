from aiohttp import web
from pprint import pprint

# Handle get tickets request
async def get_tickets(request):
    params = request.query
    print(params)
    # Get ticket information - from, to, date
    return web.Response(status=200, text="ticket list")

# Handle book ticket request
async def book_ticket(request):
    # Get ticket information - from, to, date, train
    return web.Response(status=200, text="you wanna book a ticket, huh ?")
