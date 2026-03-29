from django.apps import AppConfig

class {{ cookiecutter.package_name | camelcase }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "{{ cookiecutter.package_name }}"
    verbose_name = "{{ cookiecutter.project_name }}"
