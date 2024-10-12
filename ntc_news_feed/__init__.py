"""App declaration for ntc_news_feed."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NtcNewsFeedConfig(NautobotAppConfig):
    """App configuration for the ntc_news_feed app."""

    name = "ntc_news_feed"
    verbose_name = "Ntc News Feed"
    version = __version__
    author = "Kevin Campos"
    description = "Ntc News Feed."
    base_url = "ntc-news-feed"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:ntc_news_feed:docs"


config = NtcNewsFeedConfig  # pylint:disable=invalid-name
