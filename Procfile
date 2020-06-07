release: python manage.py makemigrations main
release: python manage.py migrate main
release: python manage.py collectstatic --noinput
release: python manage.py loaddata main.json
web: gunicorn --bind 0.0.0.0:$PORT ems.wsgi:application --log-file -