#!/bin/sh
# Wait for the database to be available (optional)
echo "Entrypoint file."

#pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Apply database migrations
echo "Applying migrations..."
python manage.py makemigrations
python manage.py makemigrations apis
python manage.py migrate


# Start the application server
echo "Starting server..."
exec gunicorn text_to_image.wsgi:application --bind 0.0.0.0:8000