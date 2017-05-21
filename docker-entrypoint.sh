#!/bin/bash
while ! nc -z db 3306; do echo "*** looks like mysql is not ready yet"; sleep 3; done
echo "+++ Mysql server is ready +++"
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files
echo Starting django dev server
python manage.py runserver 0.0.0.0:8080