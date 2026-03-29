"""
Integration Tests for Generated Django Package

Run with: uv run pytest -m integration
"""

import os
import subprocess
import pytest
from pathlib import Path


@pytest.mark.integration
class TestGeneratedProjectIntegration:
    """Minimal integration tests for generated projects."""

    def test_uv_sync_installs_dependencies(self, generated_project: Path):
        """Verify uv sync installs all dependencies."""
        env = os.environ.copy()
        env.pop("VIRTUAL_ENV", None)  # Avoid venv conflicts

        result = subprocess.run(
            ["uv", "sync"],
            cwd=generated_project,
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 0, f"uv sync failed:\n{result.stderr}"

    def test_django_check_passes(self, generated_project: Path):
        """Verify Django check passes."""
        env = os.environ.copy()
        env.pop("VIRTUAL_ENV", None)
        env["PYTHONPATH"] = str(generated_project / "src")

        subprocess.run(
            ["uv", "sync"],
            cwd=generated_project,
            capture_output=True,
            text=True,
            env=env,
            check=True,
        )

        demo_dir = generated_project / "demo_project"
        result = subprocess.run(
            ["uv", "run", "python", "manage.py", "check"],
            cwd=demo_dir,
            env=env,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Django check failed:\n{result.stderr}"

    def test_package_builds(self, generated_project: Path):
        """Verify package can be built."""
        env = os.environ.copy()
        env.pop("VIRTUAL_ENV", None)
        env["PYTHONPATH"] = str(generated_project / "src")

        subprocess.run(
            ["uv", "sync"],
            cwd=generated_project,
            capture_output=True,
            text=True,
            env=env,
            check=True,
        )

        result = subprocess.run(
            ["uv", "run", "python", "-m", "build"],
            cwd=generated_project,
            env=env,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Build failed:\n{result.stderr}"

        # Verify dist files exist
        dist_dir = generated_project / "dist"
        assert dist_dir.exists(), "dist/ directory not created"
        assert len(list(dist_dir.glob("*.whl"))) > 0, "No .whl file created"
