#! /bin/bash
set -xe

echo 'Execute Application Start Up Script'
# export DJANGO_SUPERUSER_USERNAME=$1
# export DJANGO_SUPERUSER_PASSWORD=$2
# export DJANGO_SUPERUSER_EMAIL=$3

python manage.py makemigrations
python manage.py migrate

# Use a subshell to catch an error from createsuperuser command and redirect its stderr to /dev/null
(export DJANGO_SUPERUSER_USERNAME="$1" DJANGO_SUPERUSER_PASSWORD="$2" DJANGO_SUPERUSER_EMAIL="$3"; python manage.py createsuperuser --no-input 2>/dev/null || true )

python manage.py collectstatic --noinput

uwsgi --ini uwsgi.ini
