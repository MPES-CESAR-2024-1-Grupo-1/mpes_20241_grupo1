#!/bin/sh

# Inicia o gunicorn
gunicorn --workers 3 --threads 2 -b 0.0.0.0:5000 app:app
