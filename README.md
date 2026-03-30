# Django Package Cookiecutter Template

Cookiecutter template for creating reusable Django packages with production-ready structure.

## Prerequisites

Make sure to have the following on your host:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Cookiecutter: `pip install cookiecutter`

## Quickstart

Generate a new Django package:

```bash
uv tool install cookiecutter
cookiecutter gh:TheAbhijeet/cookiecutter-django-package
```

## Configuration Options

| Prompt | Default | Description |
|--------|---------|-------------|
| `project_name` | `my-django-package` | Full name of your package (kebab-case recommended) |
| `package_name` | Auto-generated | Python importable name (auto-converted from project_name) |
| `example_project_name` | `example_project` | Name of the example_project Django project for testing |
| `author_name` | `Your Name` | Your name for package metadata |
| `author_email` | `your.email@example.com` | Your email for package metadata |
| `version` | `0.1.0` | Initial package version (semantic versioning) |
| `description` | `A reusable Django application.` | Short description for PyPI |
| `license` | `MIT` | Choose license: MIT, BSD, ISC, Apache-2.0, or GPL-3.0 |
| `python_env` | `uv` | Package manager: uv (fast) or Poetry |
| `include_drf` | `False` | Include Django REST Framework serializers and viewsets |
| `include_celery` | `False` | Include Celery configuration for async tasks |
| `include_admin_templates` | `False` | Include custom Django admin templates |
| `include_templates` | `False` | Include templates/static folders for frontend assets |

<img width="772" height="628" alt="image" src="https://github.com/user-attachments/assets/c57d4eec-40a6-49a0-8b84-9ee37f8132e3" />


## Set up the generated project:

```bash
cd <project_slug>
uv sync
uv run python example_project/manage.py migrate
uv run python example_project/manage.py runserver
```

## Features

- **src/ Layout** - Prevents accidental imports from project root
- **Demo Project** - Ready-to-run Django project for testing
- **PyPI Ready** - `pyproject.toml` configured for building
- **CI/CD** - GitHub Actions workflow included
- **Testing** - pytest with Django integration
- **Documentation** - Sphinx-ready docs folder

## Template Structure

```
cookiecutter-django-package/
├── cookiecutter.json
├── extensions.py
├── hooks/
├── {{cookiecutter.project_name}}/
│   ├── src/
│   ├── tests/
│   ├── example_project/
│   ├── docs/
│   └── pyproject.toml
├── tests/
└── pyproject.toml
```

## Development (Template)

Clone and set up the template itself:

```bash
git clone https://github.com/TheAbhijeet/cookiecutter-django-package.git
cd cookiecutter-django-package
uv sync
```

Run template tests:

```bash
uv run pytest
```

## License

MIT
