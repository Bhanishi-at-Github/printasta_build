#!/bin/bash
# Deployment script for the project

# Run the build script with the correct Python version
python -m pip install -r requirements.txt
python manage.py collectstatic

# Restart the server
python manage.py runserver