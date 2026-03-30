import os
from celery import Celery

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "{{ cookiecutter.example_project_name }}.settings"
)

app = Celery("{{ cookiecutter.package_name }}")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
