"""
Comprehensive Unit Test Suite for Django Package Cookiecutter Template
"""

import os
import sys
import json
import shutil
import subprocess
import tempfile
import pytest
from pathlib import Path
from typing import Dict, Any


# =============================================================================
# FIXTURES
# =============================================================================


@pytest.fixture(scope="module")
def template_dir() -> Path:
    """Get the template directory path."""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture(scope="module")
def cookiecutter_json(template_dir: Path) -> Dict[str, Any]:
    """Load cookiecutter.json configuration."""
    config_path = template_dir / "cookiecutter.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def temp_dir() -> Path:
    """Create a temporary directory for test outputs."""
    tmpdir = tempfile.mkdtemp()
    yield Path(tmpdir)
    try:
        shutil.rmtree(tmpdir, ignore_errors=True)
    except PermissionError:
        pass  # Windows file locks


@pytest.fixture(scope="function")
def generated_project(temp_dir: Path, template_dir: Path) -> Path:
    """Generate a project using cookiecutter and return its path."""
    shell = sys.platform.startswith("win")

    result = subprocess.run(
        ["cookiecutter", str(template_dir), "--no-input"],
        cwd=temp_dir,
        capture_output=True,
        text=True,
        shell=shell,
    )

    if result.returncode != 0:
        pytest.fail(
            f"Cookiecutter failed:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        )

    project_name = "my-django-package"
    return temp_dir / project_name


# =============================================================================
# TEST: TEMPLATE STRUCTURE
# =============================================================================


class TestTemplateStructure:
    """Test that the template has all required files and directories."""

    def test_cookiecutter_json_exists(self, template_dir: Path):
        config_path = template_dir / "cookiecutter.json"
        assert config_path.exists(), "cookiecutter.json not found"

    def test_cookiecutter_json_valid(self, template_dir: Path):
        config_path = template_dir / "cookiecutter.json"
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert isinstance(data, dict), "cookiecutter.json must be a dictionary"

    def test_template_skeleton_exists(self, template_dir: Path):
        skeleton_dir = template_dir / "{{cookiecutter.project_name}}"
        assert skeleton_dir.exists(), "Template skeleton directory not found"

    def test_src_directory_exists(self, template_dir: Path):
        src_dir = template_dir / "{{cookiecutter.project_name}}" / "src"
        assert src_dir.exists(), "src/ directory not found"

    def test_demo_project_exists(self, template_dir: Path):
        demo_dir = template_dir / "{{cookiecutter.project_name}}" / "demo_project"
        assert demo_dir.exists(), "demo_project/ directory not found"

    def test_hooks_directory_exists(self, template_dir: Path):
        hooks_dir = template_dir / "hooks"
        assert hooks_dir.exists(), "hooks/ directory not found"

    def test_post_gen_hook_exists(self, template_dir: Path):
        hook_file = template_dir / "hooks" / "post_gen_project.py"
        assert hook_file.exists(), "post_gen_project.py hook not found"

    def test_pyproject_toml_exists(self, template_dir: Path):
        pyproject = template_dir / "{{cookiecutter.project_name}}" / "pyproject.toml"
        assert pyproject.exists(), "pyproject.toml not found"


# =============================================================================
# TEST: GENERATED PROJECT STRUCTURE
# =============================================================================


class TestGeneratedProjectStructure:
    """Test the structure of generated projects."""

    def test_project_directory_created(self, generated_project: Path):
        assert generated_project.exists(), "Generated project directory not found"

    def test_src_layout_created(self, generated_project: Path):
        src_dir = generated_project / "src"
        assert src_dir.exists(), "src/ directory not created"

    def test_package_directory_created(self, generated_project: Path):
        pkg_dir = generated_project / "src" / "my_django_package"
        assert pkg_dir.exists(), "Package directory not created"

    def test_django_app_files_created(self, generated_project: Path):
        pkg_dir = generated_project / "src" / "my_django_package"
        required_files = [
            "__init__.py",
            "apps.py",
            "models.py",
            "admin.py",
            "views.py",
            "urls.py",
        ]
        for file in required_files:
            assert (pkg_dir / file).exists(), f"{file} not created"

    def test_demo_project_created(self, generated_project: Path):
        demo_dir = generated_project / "demo_project"
        assert demo_dir.exists(), "demo_project/ not created"

    def test_manage_py_exists(self, generated_project: Path):
        manage_py = generated_project / "demo_project" / "manage.py"
        assert manage_py.exists(), "manage.py not created"

    def test_pyproject_toml_created(self, generated_project: Path):
        pyproject = generated_project / "pyproject.toml"
        assert pyproject.exists(), "pyproject.toml not created"

    def test_readme_created(self, generated_project: Path):
        readme = generated_project / "README.md"
        assert readme.exists(), "README.md not created"


# =============================================================================
# TEST: GENERATED PROJECT CONTENT
# =============================================================================


class TestGeneratedProjectContent:
    """Test the content of generated project files."""

    def test_init_contains_version(self, generated_project: Path):
        init_file = generated_project / "src" / "my_django_package" / "__init__.py"
        content = init_file.read_text(encoding="utf-8")
        assert "__version__" in content, "Version not in __init__.py"

    def test_apps_py_contains_app_config(self, generated_project: Path):
        apps_file = generated_project / "src" / "my_django_package" / "apps.py"
        content = apps_file.read_text(encoding="utf-8")
        assert "AppConfig" in content, "AppConfig not in apps.py"

    def test_settings_includes_package(self, generated_project: Path):
        settings_file = generated_project / "demo_project" / "demo" / "settings.py"
        content = settings_file.read_text(encoding="utf-8")
        assert "my_django_package" in content, "Package not in INSTALLED_APPS"

    def test_pyproject_contains_django_dependency(self, generated_project: Path):
        pyproject = generated_project / "pyproject.toml"
        content = pyproject.read_text(encoding="utf-8")
        assert "Django" in content, "Django dependency not found"


# =============================================================================
# TEST: COOKIECUTTER CONFIGURATION
# =============================================================================


class TestCookiecutterConfiguration:
    """Test cookiecutter.json configuration values."""

    def test_required_fields_present(self, cookiecutter_json: Dict[str, Any]):
        required_fields = [
            "project_name",
            "package_name",
            "author_name",
            "version",
            "license",
        ]
        for field in required_fields:
            assert field in cookiecutter_json, f"Required field '{field}' missing"

    def test_version_format(self, cookiecutter_json: Dict[str, Any]):
        version = cookiecutter_json["version"]
        assert len(version.split(".")) >= 2, "Version must follow semver"

    def test_license_options(self, cookiecutter_json: Dict[str, Any]):
        licenses = cookiecutter_json["license"]
        assert isinstance(licenses, list), "License must be a list of options"
        assert len(licenses) >= 1, "Should have at least 1 license option"


# =============================================================================
# RUN TESTS
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
