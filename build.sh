#!/usr/bin/env bash
# exit on error
set -o errexit
# Configuración de variables
PYTHON_INTERPRETER=python
DJANGO_MANAGE_PY=manage.py
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py makemigrations
$PYTHON_INTERPRETER $DJANGO_MANAGE_PY createsuperuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).delete();  User.objects.create_superuser('jquintero', 'juliquinterorico@hotmail.com', 'Qwaszx.123')" | $PYTHON_INTERPRETER $DJANGO_MANAGE_PY shell
