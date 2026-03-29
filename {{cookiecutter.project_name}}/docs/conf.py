# Configuration file for the Sphinx documentation builder.

project = "{ { cookiecutter.project_name } }"
copyright = "{ { cookiecutter.version } }, { { cookiecutter.author_name } }"
author = "{ { cookiecutter.author_name } }"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
