"""
Tests to verify README.md is properly formatted.
uv run pytest tests/test_readme.py -v -s

"""

from pathlib import Path


class TestReadmeValidation:
    """Tests for README.md validation."""

    def test_readme_exists(self, generated_project: Path):
        """Verify README.md exists in generated project."""
        readme = generated_project / "README.md"
        assert readme.exists(), "README.md not found"

    def test_readme_not_empty(self, generated_project: Path):
        """Verify README.md is not empty."""
        readme = generated_project / "README.md"
        content = readme.read_text(encoding="utf-8")
        assert len(content) > 500, "README.md is too short"

    def test_readme_no_broken_cookiecutter_variables(self, generated_project: Path):
        """Verify README has no unrendered cookiecutter variables."""
        readme = generated_project / "README.md"
        content = readme.read_text(encoding="utf-8")

        # Check for broken patterns
        broken_patterns = [
            "{ {",  # Space between braces
            "} }",  # Space between braces
            "/{{ cookiecutter.",  # Unrendered variable after slash
            " {{ cookiecutter.",  # Unrendered variable with space
        ]

        for pattern in broken_patterns:
            assert pattern not in content, f"Found broken pattern in README: {pattern}"

    def test_readme_has_uv_commands(self, generated_project: Path):
        """Verify README uses uv commands."""
        readme = generated_project / "README.md"
        content = readme.read_text(encoding="utf-8")

        assert "uv sync" in content, "README should mention 'uv sync'"
        assert "uv run" in content, "README should mention 'uv run'"
        assert "uv pip install" in content, "README should mention 'uv pip install'"

    def test_readme_has_install_section(self, generated_project: Path):
        """Verify README has installation section."""
        readme = generated_project / "README.md"
        content = readme.read_text(encoding="utf-8")

        assert "## Installation" in content, "README should have Installation section"
        assert "uv pip install" in content, "Installation should use uv"

    def test_readme_has_example_project_reference(self, generated_project: Path):
        """Verify README references example_project correctly."""
        readme = generated_project / "README.md"
        content = readme.read_text(encoding="utf-8")

        assert "example_project" in content, "README should reference example_project"
        assert "example_project/example_project" not in content, (
            "README should not have nested example_project"
        )
