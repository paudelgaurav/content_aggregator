from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'

   # def ready(self):
    #    from .updater import start
     #   start()