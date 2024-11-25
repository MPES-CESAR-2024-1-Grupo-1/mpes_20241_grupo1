#!/bin/sh

# executa migrações do banco de dados
python -m flask db upgrade

# Inicia o gunicorn
gunicorn --workers 3 --threads 2 -b 0.0.0.0:5000 --log-level "debug" app:app
