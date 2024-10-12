"""
This is a hook for using logan to import settings FIRST before pytest-django.

This lets the config get setup and overlaid before anything else happens.

Use me like this:

```
$ export NAUTOBOT_CONFIG=nautobot/core/tests/nautobot_config.py
$ PYTHONPATH=. pytest --cov=nautobot -p pytest_nautobot nautobot/users/tests
```
"""

import os

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config, parser, args):
    from nautobot import setup

    setup()
