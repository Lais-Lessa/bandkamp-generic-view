#!/usr/bin/env bash
# exit on error
set -o errexit 

pip install -r requirements.txt #vai instalar todas as dependências
python manage.py collectstatic --no-input #cria a pasta dos arquivos estaticos
python manage.py migrate #para apliar as migrações
 