#!/usr/bin/env bash
# exit on error
set -o errexit

#!/bin/bash
ls
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

    
wget -q -O LibreOffice_24.2.1_Linux_x86-64_deb.tar.gz https://download.documentfoundation.org/libreoffice/stable/24.2.1/deb/x86_64/LibreOffice_24.2.1_Linux_x86-64_deb.tar.gz && \
tar -zxvf LibreOffice_24.2.1_Linux_x86-64_deb.tar.gz && \
cd LibreOffice_24.2.1.2_Linux_x86-64_deb/DEBS/ && \
sudo dpkg -i *.deb && \
sudo apt-get install -f

cd ../../
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* wkhtmltopdf.deb LibreOffice_24.2.1_Linux_x86-64_deb.tar.gz LibreOffice_24.2.1_Linux_x86-64_deb


# Configuración de variables
PYTHON_INTERPRETER=python
DJANGO_MANAGE_PY=manage.py
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).delete();  User.objects.create_superuser('jquintero', 'juliquinterorico@hotmail.com', 'Qwaszx.123')" | python manage.py shell
