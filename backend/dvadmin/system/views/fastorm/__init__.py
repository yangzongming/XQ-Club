from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'
    def ready(self):
        print("FUCK")