# Django ChatterBot Terminal Client

This project provides a terminal chatbot as a custom Django management command. ChatterBot stores learned statements in a local SQLite database and selects responses from trained conversations.

## Setup

```bash
python -m venv .venv
```

Activate the virtual environment and install the packages:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python manage.py chat
```

Enter `exit` or `quit` to end the conversation. After the initial training run, use `python manage.py chat --no-train` to load the existing knowledge database without repeating training.

## GitHub submission

Create a GitHub repository, add the project files, commit them, and replace the placeholder repository URL in the Word report with your actual GitHub link.
