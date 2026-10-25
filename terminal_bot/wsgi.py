"""WSGI configuration for completeness in the Django project."""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "terminal_bot.settings")
application = get_wsgi_application()
