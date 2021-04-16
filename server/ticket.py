from aiohttp import web
from pprint import pprint

# Handle get tickets request
async def get_tickets(request):
    db = request.app['db']
    data = await request.json()
    _from = data['from']
    _to = data['to']
    date = data['date']
    if (date == ""):
        # search based on FROM and TO only
        cmd = f"SELECT * FROM Tickets WHERE _from LIKE '{_from}' AND _to LIKE '{_to}'"
    else:
        # search based on FROM and TO and date too
        cmd = f"SELECT * FROM Tickets WHERE _from LIKE '{_from}' AND _to LIKE '{_to}'"
    print(cmd)
    cursor = db.cursor()
    result = cursor.execute(cmd).fetchall()
    print(result)
    # Get ticket information - from, to, date
    return web.json_response({})

# Handle book ticket request
async def book_ticket(request):
    # Get ticket information - from, to, date, train
    return web.Response(status=200, text="you wanna book a ticket, huh ?")
