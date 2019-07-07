python manage.py makemigrations &&
python manage.py migrate &&
gunicorn cygSqlite.wsgi:application -c gunicorn.conf.py
