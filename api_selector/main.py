from aiohttp import web
import aiohttp
from middlewares import auth_middleware, urlresolver_middleware

routes = web.RouteTableDef()

async def handle_all_requests(request):
    session = aiohttp.ClientSession()
    async with session.request(method=request.method, url="http://localhost:8081/api/client/avaliable_urls") as status:
        data = await status.text()
        print(data)
    await session.close()
    return web.Response(text=data)


app = web.Application()
app.middlewares.append(urlresolver_middleware)
app.middlewares.append(auth_middleware)
app.router.add_route('*', '/{path_info:.*}', handle_all_requests)
web.run_app(app)