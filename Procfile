release: python manage.py migrate
web: gunicorn abelsantana.wsgi --log-file -
worker: celery -A abelsantana worker -B
