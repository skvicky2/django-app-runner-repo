#!/bin/bash
python manage.py migrate --noinput && gunicorn --workers 2 understand_science.wsgi
