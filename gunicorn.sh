#!/bin/bash

cd /netseen
mkdir logs
python manage.py createdb
python manage.py create_admin

#/usr/local/bin/gunicorn config.wsgi:application -w 2 -b :8000
gunicorn --log-level info --log-file=/netseen/logs/gunicorn.log --workers 4 --name project_gunicorn -b 0.0.0.0:8000 --reload netseen.wsgi:application
