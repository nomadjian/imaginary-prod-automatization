from aiohttp import web


import json
routes = web.RouteTableDef()

@routes.get('/api/nomenclature/avaliable_urls')
async def get_paths(request):
    data = [{"path":route.path, "method":route.method} for route in routes]
    return web.Response(body=json.dumps(data), status=200)

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8081)