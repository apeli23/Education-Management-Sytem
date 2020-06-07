find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py collectstatic --noinput
python manage.py dumpdata main --exclude auth --indent 2  > main.json
