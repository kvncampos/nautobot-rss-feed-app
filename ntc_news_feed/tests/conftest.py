# ntc_news_feed/tests/conftest.py

import os

import pytest
from django.conf import settings
from dotenv import load_dotenv


@pytest.fixture(autouse=True)
def enable_ntc_news_feed_app(settings):
    """
    Fixture to ensure the ntc_news_feed app is enabled during tests.
    """
    if "ntc_news_feed" not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS.append("ntc_news_feed")


# Define the path to your .env file
dotenv_path = os.path.join(
    os.path.dirname(__file__), "../../development/development.env"
)

# Load the environment variables from the .env file
load_dotenv(dotenv_path)


@pytest.fixture(autouse=True)
def setup_environment():
    # Verify that the environment variables are loaded correctly
    print(f"DB_NAME: {os.getenv('NAUTOBOT_DB_NAME')}")
    print(f"DB_USER: {os.getenv('NAUTOBOT_DB_USER')}")
    print(f"DB_PASSWORD: {os.getenv('NAUTOBOT_DB_PASSWORD')}")
    print(f"DB_HOST: {os.getenv('NAUTOBOT_DB_HOST')}")
    print(f"DB_PORT: {os.getenv('NAUTOBOT_DB_PORT')}")
