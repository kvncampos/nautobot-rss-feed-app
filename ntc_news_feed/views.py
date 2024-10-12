# ntc_news_feed/views.py
from django.shortcuts import render
from nautobot.core.views.generic import ObjectListView

# ntc_news_feed/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .homepage import get_ntc_blog_data
from .models import RSSFeed
from .serializers import (
    RSSFeedSerializer,
)

# You'll need to create a serializer for this
from .tables import RSSFeedTable


# API ViewSet for RSSFeed
class RSSFeedViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing, editing, and deleting RSS feeds."""

    queryset = RSSFeed.objects.all()
    serializer_class = RSSFeedSerializer

    @action(detail=False, methods=["get"])
    def active(self, request):
        """Custom action to retrieve only active RSS feeds."""
        active_feeds = self.queryset.filter(active=True)
        serializer = self.get_serializer(active_feeds, many=True)
        return Response(serializer.data)


# Your existing views remain here for the non-API views
def custom_ntc_blog_feed(request):
    """Render a custom Network to Code blog feed page with the latest articles."""
    items = get_ntc_blog_data(request)
    context = {"articles": items}
    return render(request, "ntc_news_feed/custom_blog_feed.html", context)


# List View for managing RSS Feeds
class ManageRSSFeedsView(ObjectListView):
    queryset = RSSFeed.objects.all()
    table = RSSFeedTable
    template_name = "ntc_news_feed/manage_rss_feeds.html"
