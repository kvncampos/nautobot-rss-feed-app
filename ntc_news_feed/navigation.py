from nautobot.core.apps import (
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuItem,
    NavMenuImportButton,
    NavMenuTab,
)

menu_items = [
    NavMenuTab(
        name="NTC News Feed",
        weight=1000,
        groups=(
            NavMenuGroup(
                name="RSS Feeds",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:ntc_news_feed:rssfeed_add",
                        name="Add RSS Feed",
                        permissions=["ntc_news_feed.add_rssfeed"],
                        weight=100,
                    ),
                    NavMenuItem(
                        link="plugins:ntc_news_feed:custom_ntc_blog_feed",
                        name="View All RSS Feeds",
                        permissions=["ntc_news_feed.view_rssfeed"],
                        weight=200,
                    ),
                    NavMenuItem(
                        link="plugins:ntc_news_feed:manage_rssfeed",
                        name="Manage RSS Feeds",
                        permissions=["ntc_news_feed.view_rssfeed"],
                        weight=200,
                    ),
                ),
            ),
        ),
    ),
]
