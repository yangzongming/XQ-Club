from django.apps import AppConfig


from backend.dvadmin.system.views.fastorm import orm

class SystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dvadmin.system'

    def ready(self):
        import asyncio
        loop = asyncio.get_event_loop()
        yield from orm.create_pool(loop=loop)
