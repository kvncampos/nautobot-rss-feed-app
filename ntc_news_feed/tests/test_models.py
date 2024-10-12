import pytest

from ntc_news_feed.models import RSSFeed


@pytest.mark.django_db
def test_rssfeed_str():
    """Test the string representation of the RSSFeed model."""
    rss_feed = RSSFeed(name="Test Feed", url="http://test.com", active=True)
    rss_feed.save()
    assert str(rss_feed) == "Test Feed"
