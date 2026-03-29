# Django Package Cookiecutter Template

Cookiecutter template for creating reusable Django packages with production-ready structure.

## Prerequisites

Make sure to have the following on your host:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Cookiecutter: `pip install cookiecutter`

## Quickstart

Generate a new Django package:

```bash
cookiecutter gh:your-username/cookiecutter-django-package
```

Set up the generated project:

```bash
cd <project_slug>
uv sync
uv run python demo_project/manage.py migrate
uv run python demo_project/manage.py runserver
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
│   ├── demo_project/
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

## Configuration Options

| Prompt | Default | Description |
|--------|---------|-------------|
| `project_name` | `my-django-package` | Package name |
| `package_name` | Auto-generated | Python import name |
| `author_name` | `Your Name` | Author |
| `license` | `MIT` | License type |
| `include_demo` | `True` | Include demo project |
| `include_drf` | `False` | Django REST Framework |
| `include_celery` | `False` | Celery support |

## License

MIT
