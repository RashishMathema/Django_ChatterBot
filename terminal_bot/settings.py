"""Minimal Django settings for the ChatterBot terminal client."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# This classroom application runs locally and does not expose a web server.
SECRET_KEY = "classroom-terminal-chatbot-development-key"
DEBUG = True
ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "chatbot_app.apps.ChatbotAppConfig",
]

MIDDLEWARE: list[str] = []
ROOT_URLCONF = "terminal_bot.urls"
TEMPLATES: list[dict] = []
WSGI_APPLICATION = "terminal_bot.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True

# ChatterBot stores learned statements separately from Django's database.
CHATTERBOT_DATABASE_URI = f"sqlite:///{BASE_DIR / 'chatterbot.sqlite3'}"
