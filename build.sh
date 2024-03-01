#!/usr/bin/env bash
# exit on error
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

# Descarga e instala LibreOffice
wget -q -O LibreOffice.tar.gz https://download.documentfoundation.org/libreoffice/stable/7.2.1/deb/x86_64/LibreOffice_7.2.1_Linux_x86-64_deb.tar.gz && \
tar -zxvf LibreOffice.tar.gz && \
cd LibreOffice_7.2.1.2_Linux_x86-64_deb/DEBS/ && \
sudo dpkg -i *.deb && \
sudo apt-get install -f

# Limpia los archivos temporales
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* LibreOffice.tar.gz LibreOffice_7.2.1.2_Linux_x86-64_deb

# Configura las variables
PYTHON_INTERPRETER=python
DJANGO_MANAGE_PY=manage.py

# Instala las dependencias de Python
pip install -r requirements.txt

# Configuración adicional de Django
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
$PYTHON_INTERPRETER $DJANGO_MANAGE_PY createsuperuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).delete();  User.objects.create_superuser('jquintero', 'juliquinterorico@hotmail.com', 'Qwaszx.123')" | $PYTHON_INTERPRETER $DJANGO_MANAGE_PY shell