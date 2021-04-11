from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery()
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_routes = {
    'products.tasks.start_handler_product': {
        'queue': 'products',
        'routing_key': 'products.tasks.start_handler_product'
    },
}

app.conf.beat_schedule = {
    'start_parsing_shop': {
        'task': 'twenty_first_century.tasks.start_parsing_shop',
        'schedule': crontab(),
    }
}

