#!/usr/bin/env python
"""Django command-line utility for the terminal chatbot project."""

import os
import sys


def main() -> None:
    """Run Django administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "terminal_bot.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django is not installed. Run: python -m pip install -r requirements.txt"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
