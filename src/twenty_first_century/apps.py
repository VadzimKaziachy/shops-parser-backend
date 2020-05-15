from django.apps import AppConfig


class TwentyFirstCenturyConfig(AppConfig):
    name = 'twenty_first_century'
    verbose_name = '21vek.by'

    def ready(self):
        from . import signals