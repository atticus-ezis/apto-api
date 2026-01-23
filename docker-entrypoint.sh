#!/bin/bash
set -e

echo "Running database migrations..."
python manage.py migrate

echo "Running tests..."
python manage.py test

echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
