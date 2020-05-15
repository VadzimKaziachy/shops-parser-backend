from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from .settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('app', backend=CELERY_RESULT_BACKEND, broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings')

app.conf.task_routes = {
    'twenty_first_century.tasks.start_handler_product': {
        'queue': 'start_handler_product_queue'
    },
}

app.conf.beat_schedule = {
    'start_parsing_shop': {
        'task': 'twenty_first_century.tasks.start_parsing_shop',
        'schedule': crontab(),
    }
}

