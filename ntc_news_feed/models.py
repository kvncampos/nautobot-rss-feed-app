from django.db import models
from nautobot.core.models import BaseModel


class RSSFeed(BaseModel):
    """Model for storing RSS feed details."""

    name = models.CharField(
        max_length=100, unique=True, help_text="Name of the RSS feed."
    )
    url = models.URLField(unique=True, help_text="URL of the RSS feed.")
    active = models.BooleanField(
        default=True, help_text="Whether the RSS feed is active or not."
    )

    def __str__(self):
        return self.name
