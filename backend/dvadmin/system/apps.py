from django.apps import AppConfig


from .views.fastorm import orm
import asyncio

class SystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dvadmin.system'

    @asyncio.coroutine
    def init1(loop):
        yield from orm.create_pool(loop=loop,{})


    def ready(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(init1(loop))
        loop.run_forever()
