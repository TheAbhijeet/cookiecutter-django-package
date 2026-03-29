# tests/conftest.py
import pytest
import json
import sys
from pathlib import Path


@pytest.fixture(scope="module")
def template_dir() -> Path:
    """Get the template directory path."""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture(scope="module")
def cookiecutter_json(template_dir: Path) -> dict:
    """Load cookiecutter.json configuration."""
    config_path = template_dir / "cookiecutter.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def temp_dir() -> Path:
    """Create a temporary directory for test outputs."""
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()
    yield Path(tmpdir)
    try:
        shutil.rmtree(tmpdir, ignore_errors=True)
    except PermissionError:
        # Windows might have file locks
        pass


@pytest.fixture(scope="function")
def generated_project(temp_dir: Path, template_dir: Path) -> Path:
    """Generate a project using cookiecutter and return its path."""
    import subprocess

    # Use shell=True on Windows for better path handling
    shell = sys.platform.startswith("win")

    result = subprocess.run(
        ["cookiecutter", str(template_dir), "--no-input"],
        cwd=temp_dir,
        capture_output=True,
        text=True,
        shell=shell,
    )

    if result.returncode != 0:
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        raise RuntimeError(f"Cookiecutter failed: {result.stderr}")

    project_name = "my-django-package"
    return temp_dir / project_name
