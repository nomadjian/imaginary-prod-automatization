from aiohttp import web
import redis


NOAUTH_PATHS = ['/login', '/auth', '/']

rds = redis.Redis()

async def auth_middleware(app, handler):
    async def middleware_handler(request):
        if request.path in NOAUTH_PATHS:
            return await handler(request)
        token = request.headers.get('Authorization', None)
        if token:
            user = rds.get('token')
            if user:
                return await handler(request)
            else:
                return web.Response(text='INVALID TOKEN', status=403)        
        else:
            return web.Response(text='TOKEN REQUIRED', status=401)
    return middleware_handler
    