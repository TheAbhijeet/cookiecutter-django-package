# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg)](https://pypi.org/project/{{ cookiecutter.package_name }}/))
[![License](https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}.svg)](https://pypi.org/project/{{ cookiecutter.package_name }}/))

## Installation

```bash
pip install {{ cookiecutter.package_name }}
or 
uv add {{ cookiecutter.package_name }}
```

## Development Setup

### 1. Clone and Enter Directory
```bash
cd {{ cookiecutter.project_name }}
```

### 2. Install Package

```bash
uv sync
```


### 3. Run example_project
```bash
cd example_project
uv run python example_project/manage.py migrate
uv run python example_project/manage.py runserver
```

### 4. Run Tests
```bash
uv run pytest
```

## Publishing to PyPI

### 1. Build
```bash
uv pip install build twine
uv run python -m build
```

### 2. TestPyPI
```bash
uv run twine upload --repository testpypi dist/*
```

### 3. PyPI
```bash
uv run twine upload dist/*
```

## Documentation

See `docs/` directory for detailed documentation.

## Contributing

See `CONTRIBUTING.md` for guidelines.

## License

{{ cookiecutter.license }}
