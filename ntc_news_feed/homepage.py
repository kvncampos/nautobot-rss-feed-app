from datetime import datetime

import dateparser
import feedparser
import requests
from bs4 import BeautifulSoup
from nautobot.core.apps import HomePagePanel

from .models import RSSFeed


def get_ntc_blog_data(request):
    """Fetch and process the latest articles from the Network to Code blog."""

    def _hardcode_description(article):
        """Modify article description if it matches specific title."""
        if "Last Month in Nautobot" in article["title"]:
            article["description"] = (
                "Join us as we celebrate the latest milestones, new releases, and community contributions in Nautobot—showcasing the innovation, collaboration, and achievements that drive our vibrant community forward!"
            )
        return article

    blog_url = "https://blog.networktocode.com/"

    # Fetch the blog articles
    try:
        response = requests.get(blog_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    blog_posts = soup.find_all(
        "div", class_="vc_row wpb_row section vc_row-fluid grid_section"
    )

    # Extract article details
    articles = []
    for post in blog_posts:
        title_tag = post.find("h2")
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = (
                title_tag.find("a", href=True)["href"]
                if title_tag.find("a", href=True)
                else None
            )
            if link and not link.startswith("http"):
                link = f"https://blog.networktocode.com{link}"
        else:
            title, link = "No Title", "#"

        pubdate_tag = post.find("h6")
        if pubdate_tag:
            pubdate_text = pubdate_tag.get_text(strip=True)
            date_part = pubdate_text.split("|")[0].strip()
            author = pubdate_text.split("|")[1].strip().replace("-", "").strip()
            pubdate = dateparser.parse(date_part)
            formatted_pubdate = pubdate.strftime("%b. %d, %Y") if pubdate else "No Date"
        else:
            formatted_pubdate = datetime.now().strftime("%b. %d, %Y")

        description_tag = post.find("p")
        description = (
            description_tag.get_text(strip=True)
            if description_tag
            else "No Description"
        )

        article = {
            "title": title,
            "link": link,
            "description": description,
            "published": formatted_pubdate,
            "author": author,
        }

        # Use the helper function to modify the description if applicable
        articles.append(_hardcode_description(article))

    return articles


def get_custom_rss_feed_data(request):
    """Fetch and process RSS feeds using feedparser."""
    articles = []

    # Get all active RSS feeds from the database
    feeds = RSSFeed.objects.filter(active=True)
    for feed in feeds:
        parsed_feed = feedparser.parse(feed.url)
        for entry in parsed_feed.entries:
            # Extract the necessary fields from the feed entries
            article = {
                "title": entry.get("title", "No Title"),
                "link": entry.get("link", "#"),
                "description": entry.get("summary", "No Description"),
                "author": entry.get("author", "Unknown"),
                "published": entry.get("published", "No Date"),
            }
            articles.append(article)
    return articles


def get_combined_articles(request):
    """Fetch articles from both NTC blog and custom RSS feeds."""
    # Get articles from the NTC blog
    ntc_articles = get_ntc_blog_data(request)

    # Get articles from custom RSS feeds
    custom_rss_articles = get_custom_rss_feed_data(request)

    # Combine both sources into a single list
    combined_articles = ntc_articles + custom_rss_articles

    # Sort articles by published date, if present (optional)
    combined_articles.sort(key=lambda x: x.get("published", ""), reverse=True)

    return combined_articles


# Define the HomePagePanel layout using the custom_data attribute
layout = (
    HomePagePanel(
        name="Latest NTC News",
        custom_template="home_ntc_widget.html",
        custom_data={"articles": get_combined_articles},
        permissions=["ntc_news_feed.view_rssfeed"],
        weight=1,
    ),
)
