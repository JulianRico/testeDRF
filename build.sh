#!/usr/bin/env bash
# exit on error
set -o errexit

#!/bin/bash

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

# Descarga e instala wkhtmltopdf
wget -q -O wkhtmltopdf.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb && \
    dpkg -i wkhtmltopdf.deb && \
    apt-get install -f
    
wget -q -O LibreOffice_7.6.5_Linux_x86-64_deb.tar.gz https://www.libreoffice.org/donate/dl/deb-x86_64/7.6.5/es/LibreOffice_7.6.5_Linux_x86-64_deb.tar.gz && \
tar -zxvf LibreOffice_7.6.5_Linux_x86-64_deb.tar.gz && \
cd LibreOffice_7.3.0.0_Linux_x86-64_deb/DEBS && \
sudo dpkg -i *.deb && \
sudo apt-get install -f


apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* wkhtmltopdf.deb LibreOffice_7.6.5_Linux_x86-64_deb.tar.gz LibreOffice_7.6.5_Linux_x86-64_deb


# Configuración de variables
PYTHON_INTERPRETER=python
DJANGO_MANAGE_PY=manage.py
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
$PYTHON_INTERPRETER $DJANGO_MANAGE_PY createsuperuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).delete();  User.objects.create_superuser('jquintero', 'juliquinterorico@hotmail.com', 'Qwaszx.123')" | $PYTHON_INTERPRETER $DJANGO_MANAGE_PY shell
