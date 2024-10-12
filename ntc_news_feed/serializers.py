# ntc_news_feed/serializers.py
from rest_framework import serializers

from .models import RSSFeed


class RSSFeedSerializer(serializers.ModelSerializer):
    """Serializer for the RSSFeed model."""

    class Meta:
        model = RSSFeed
        fields = "__all__"
