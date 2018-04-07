#!/usr/bin/env bash
source env/bin/activate

cd project/myshop
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
