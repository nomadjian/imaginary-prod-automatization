from aiohttp import web
from permission_middleware import auth_middleware

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text='Ello, GuvNor')

@routes.get('/login')
async def login(request):
    return web.Response(text='You logined')

app = web.Application()
app.middlewares.append(auth_middleware)
app.add_routes(routes)
web.run_app(app)