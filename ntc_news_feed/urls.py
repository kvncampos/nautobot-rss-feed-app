# ntc_news_feed/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RSSFeedViewSet, custom_ntc_blog_feed

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"rssfeeds", RSSFeedViewSet, basename="rssfeed")

# Define URL patterns using the router
urlpatterns = [
    path("", custom_ntc_blog_feed, name="custom_ntc_blog_feed"),  # Non-API view
    path("", include(router.urls)),  # Include the router's URL patterns
]
