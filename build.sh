#!/usr/bin/env bash
set -o errexit

# Actualiza los repositorios e instala las dependencias necesarias
apt-get update && apt-get install -y \
    wget \
    xvfb \
    libfontconfig \
    libjpeg-turbo8 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base

# Instala LibreOffice
apt-get install -y libreoffice

# Limpia el sistema
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Instala las dependencias de Python
PYTHON_INTERPRETER=python
DJANGO_MANAGE_PY=manage.py
pip install -r requirements.txt

# Ejecuta comandos de Django
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

# Crea un superusuario de Django (cambia los valores según sea necesario)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).delete();  User.objects.create_superuser('jquintero', 'juliquinterorico@hotmail.com', 'Qwaszx.123')" | $PYTHON_INTERPRETER $DJANGO_MANAGE_PY shell