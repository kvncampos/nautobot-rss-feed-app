import django_tables2 as tables
from nautobot.core.tables import BaseTable, ButtonsColumn

from .models import RSSFeed


# Define a table for displaying the RSSFeed objects
class RSSFeedTable(BaseTable):
    """Table definition for displaying RSS Feed objects."""

    name = tables.Column(verbose_name="Name")
    url = tables.Column(verbose_name="Feed URL")
    active = tables.BooleanColumn(verbose_name="Active")
    actions = ButtonsColumn(
        model=RSSFeed, buttons=("edit", "delete"), verbose_name="Actions"
    )

    class Meta(BaseTable.Meta):
        model = RSSFeed
        fields = ("name", "url", "active", "actions")
        default_columns = ("name", "url", "active", "actions")
