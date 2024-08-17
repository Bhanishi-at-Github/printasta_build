"""
WSGI config for printasta project.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'printasta.settings')

application = get_wsgi_application()


# Vercel Setting

app = application