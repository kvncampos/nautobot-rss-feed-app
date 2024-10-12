"""Custom Jinja2 filters for templates."""

import re

from django import template
from django_jinja import library

register = template.Library()


@library.filter()
@register.filter()
def firstline(value):
    """Return the first sentence of a given string."""
    if not isinstance(value, str):
        return value
    # Split at the first occurrence of . ! or ?
    match = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", value)
    return match[0] if match else value
