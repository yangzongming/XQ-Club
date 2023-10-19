import asyncio
from ..fastorm import orm
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        print(123)
        loop = asyncio.get_event_loop()
        yield from orm.create_pool(loop=loop)