import asyncio
from backend.dvadmin.system.views.fastorm import orm


def start():
    print(123)
    loop = asyncio.get_event_loop()
    yield from orm.create_pool(loop=loop)