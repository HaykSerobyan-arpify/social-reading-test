#!/usr/bin/env sh

sudo apt-get install python3-opencv

python manage.py collectstatic --no-input

gunicorn app.wsgi:application --bind 0.0.0.0:8000