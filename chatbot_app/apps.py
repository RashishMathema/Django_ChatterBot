"""Django application configuration."""

from django.apps import AppConfig


class ChatbotAppConfig(AppConfig):
    """Register the terminal chatbot application with Django."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "chatbot_app"
