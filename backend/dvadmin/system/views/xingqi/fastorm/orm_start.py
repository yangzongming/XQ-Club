import asyncio
from ..fastorm import orm
from django.apps import AppConfig

def start():
    print(123)
    loop = asyncio.get_event_loop()
    yield from orm.create_pool(loop=loop)