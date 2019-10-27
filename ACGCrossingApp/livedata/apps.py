from django.apps import AppConfig
import time 

class LivedataConfig(AppConfig):
    name = 'livedata'

    def ready(self):
        from .task_scheduler import start
        start()