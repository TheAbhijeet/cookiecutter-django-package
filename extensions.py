from jinja2.ext import Extension


class CamelcaseExtension(Extension):
    """Custom Cookiecutter extension for camelcase filter."""

    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["camelcase"] = self.camelcase_filter

    @staticmethod
    def camelcase_filter(value: str) -> str:
        """Convert string to CamelCase."""
        import re

        words = re.split(r"[_\-\s]", value)
        return "".join(word.capitalize() for word in words if word)
