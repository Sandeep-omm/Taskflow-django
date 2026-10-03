# Taskflow

A small Django task manager with individual accounts and a responsive workspace. Each task has a status, priority, optional due date, and description. Users can search, filter, edit, complete, and delete their own tasks.

## Requirements

- Python 3.10 or later
- pip

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ and create an account. The first visit redirects to login; use **Create an account** to sign up. To administer users and tasks, create an admin account with `python manage.py createsuperuser` and open http://127.0.0.1:8000/admin/.

## Project layout

- `taskmanager/` — Django settings and application entry points
- `tasks/` — task model, forms, views, URLs, and initial database migration
- `templates/` — task workspace and account pages
- `static/css/app.css` — responsive interface styling

SQLite data is stored in `db.sqlite3` in the project root. The included secret key and `DEBUG = True` are for local development only; replace them with environment-based settings before deploying this project.
