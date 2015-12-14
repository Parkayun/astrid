import asyncio
from datetime import datetime

from aiohttp.web import WebSocketResponse


@asyncio.coroutine
def request_logger(app, handler):
    @asyncio.coroutine
    def middleware(request):
        request.app.stdout.write("".join((datetime.now().__str__(), request.path)))
        return (yield from handler(request))
    return middleware



@asyncio.coroutine
def web_socket(app, handler):
    @asyncio.coroutine
    def middleware(request):
        if handler.__name__ in getattr(app, 'websocket_handlers', []):
            return (yield from handler(request, WebSocketResponse()))
        return (yield from handler(request))
    return middleware
