#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --http :8000 --module core.wsgi
exec "$@"