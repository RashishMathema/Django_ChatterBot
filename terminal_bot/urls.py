"""URL configuration required by Django, although this app is terminal-only."""

from django.urls import path


urlpatterns = [path("", lambda request: None, name="terminal-only")]
