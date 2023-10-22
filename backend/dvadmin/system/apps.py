from django.apps import AppConfig


from .views.fastorm import orm
import asyncio

class SystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dvadmin.system'

    def ready(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(initA(loop))
        loop.run_forever()

        @asyncio.coroutine
        def initA(loop):
            yield from orm.create_pool(loop=loop)
            return 1
