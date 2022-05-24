#!/bin/bash -x
python manage.py makemigrations api || exit 1
python manage.py migrate || exit 1
python manage.py loaddata organization
python manage.py initsuperuser
python manage.py runserver 0.0.0.0:8090
exec "$@"
