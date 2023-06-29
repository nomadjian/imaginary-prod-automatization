from aiohttp import web
import redis


NOAUTH_PATHS = ['/login', '/auth', '/api/client/']
AVALIABLE_MODULES = ['client','sector','nomeclature','history']

rds = redis.Redis()

async def auth_middleware(app, handler):
    async def middleware_handler(request):
        print('auth_middleware is working')
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
    

async def urlresolver_middleware(app, handler):
    async def middleware_handler(request):
        parsed_uri = (request.path).split('/')[1:]
        if parsed_uri[0] == 'api':
            if parsed_uri[1] in AVALIABLE_MODULES:
                return await handler(request)
            else:
                return web.Response(text='Invalid or unavaliable service', status=404)    
        else:
            return web.Response(text='Invalid URL', status=404)
    return middleware_handler