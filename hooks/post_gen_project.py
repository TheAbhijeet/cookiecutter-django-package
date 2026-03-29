import os
import shutil
from pathlib import Path


def delete_file(filepath):
    """Delete a file if it exists."""
    path = Path(filepath)
    if path.exists():
        path.unlink()
        print(f"Deleted: {filepath}")


def delete_directory(filepath):
    """Delete a directory and all contents."""
    path = Path(filepath)
    if path.exists():
        shutil.rmtree(filepath)
        print(f"Deleted directory: {filepath}")


def main():
    """Run post-generation cleanup."""
    if "{{ cookiecutter.include_celery }}" == "False":
        delete_file("src/{{ cookiecutter.package_name }}/celery.py")

    if "{{ cookiecutter.include_templates }}" == "False":
        delete_directory("src/{{ cookiecutter.package_name }}/templates")

    if "{{ cookiecutter.include_demo }}" == "False":
        delete_directory("demo_project")

    print("Post-generation cleanup completed successfully.")


if __name__ == "__main__":
    main()
