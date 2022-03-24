# Inncicla
Install Django, Django REST Framework, Django Channels, channel_redis, pytest-asyncio, pytest-django, Pillow, djangorestframework-simplejwt, and Psycopg2. Then, create a new Django project and app.

(env)$ pip install \
       Django==4.0 \
       djangorestframework==3.13.1 \
       channels==3.0.4 \
       channels-redis==3.3.1 \
       pytest-asyncio==0.16.0 \
       pytest-django==4.5.2 \
       Pillow==8.4.0 \
       djangorestframework-simplejwt==5.0.0 \
       psycopg2-binary==2.9.2

(env)$ django-admin startproject taxi .
(env)$ python manage.py startapp trips
