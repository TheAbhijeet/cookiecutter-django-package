# { { cookiecutter.project_name } }

{ { cookiecutter.description } }

[![PyPI](https://img.shields.io/pypi/v/{ { cookiecutter.package_name } }.svg)](https://pypi.org/project/{ { cookiecutter.package_name } }/))
[![License](https://img.shields.io/pypi/l/{ { cookiecutter.package_name } }.svg)](https://pypi.org/project/{ { cookiecutter.package_name } }/))

## Installation

```bash
pip install { { cookiecutter.package_name } }
```

## Development Setup

### 1. Clone and Enter Directory
```bash
cd { { cookiecutter.project_name } }
```

### 2. Create Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Package
```bash
pip install -e src/
```

### 4. Run Demo
```bash
cd demo_project
python manage.py migrate
python manage.py runserver
```

### 5. Run Tests
```bash
pytest
```

## Publishing to PyPI

### 1. Build
```bash
pip install build twine
python -m build
```

### 2. TestPyPI
```bash
twine upload --repository testpypi dist/*
```

### 3. PyPI
```bash
twine upload dist/*
```

## Documentation

See `docs/` directory for detailed documentation.

## Contributing

See `CONTRIBUTING.md` for guidelines.

## License

{ { cookiecutter.license } }
