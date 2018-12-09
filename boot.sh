#!/bin/sh
python manage.py migrate
python manage.py collectstatic
python manage.py add_superuser
python manage.py fake

exec gunicorn -w 8 -b :8000 --access-logfile - --error-logfile - project.wsgi:application