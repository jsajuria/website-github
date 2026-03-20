#!/usr/bin/env python3
"""
Syncs Javier Sajuria's La Tercera columns to the Hugo blog.
Fetches the author page, finds new articles not yet in the blog,
extracts the full text from each article's JSON-LD data, and
generates properly formatted markdown files.
"""

import glob
import json
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

AUTHOR_URL = "https://www.latercera.com/autor/javier-sajuria/"
POSTS_DIR = "exampleSite/content/posts"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def get_existing_slugs():
    """Return the set of slugs already present in the posts directory."""
    slugs = set()
    for filepath in glob.glob(os.path.join(POSTS_DIR, "*.es-cl.md")):
        basename = os.path.basename(filepath)
        # Filename format: YYYY-MM-DD-slug.es-cl.md
        # Strip date prefix and .es-cl.md suffix to get the slug
        match = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)\.es-cl\.md$", basename)
        if match:
            slugs.add(match.group(1))
        else:
            # Handle files without date prefix
            slugs.add(basename.replace(".es-cl.md", ""))
    return slugs


def get_author_page_articles():
    """Scrape the author page and return a list of article URLs."""
    print(f"Fetching author page: {AUTHOR_URL}")
    resp = requests.get(AUTHOR_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    urls = []
    seen = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Normalise relative URLs
        if href.startswith("/"):
            href = "https://www.latercera.com" + href
        if "/opinion/noticia/" in href and href not in seen:
            seen.add(href)
            urls.append(href)

    print(f"Found {len(urls)} article links on author page.")
    return urls


def slug_from_url(url):
    """Extract the slug (last path segment) from a La Tercera article URL."""
    return url.rstrip("/").split("/")[-1]


def fetch_article(url):
    """
    Fetch a La Tercera article and extract metadata + body text.
    Returns a dict or None if extraction fails.
    """
    print(f"  Fetching: {url}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  WARNING: Could not fetch {url}: {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Try JSON-LD structured data first (most reliable)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
            # Handle both single objects and arrays
            if isinstance(data, list):
                data = next((d for d in data if d.get("@type") == "NewsArticle"), None)
                if not data:
                    continue
            if data.get("@type") == "NewsArticle":
                title = data.get("headline", "").strip()
                date_raw = data.get("datePublished", "")
                body = data.get("articleBody", "").strip()

                if not title or not body:
                    print(f"  WARNING: JSON-LD found but title or body is empty for {url}")
                    return None

                # Normalise date to YYYY-MM-DD
                date = date_raw[:10] if date_raw else ""
                if not re.match(r"\d{4}-\d{2}-\d{2}", date):
                    print(f"  WARNING: Unexpected date format '{date_raw}' for {url}")
                    return None

                # Convert plain-text body paragraphs to markdown paragraphs
                paragraphs = [p.strip() for p in body.split("\n") if p.strip()]
                body_md = "\n\n".join(paragraphs)

                return {
                    "title": title,
                    "date": date,
                    "body": body_md,
                    "url": url,
                }
        except (json.JSONDecodeError, AttributeError):
            continue

    print(f"  WARNING: Could not extract article data from {url}")
    return None


def escape_toml_string(s):
    """Escape double quotes and backslashes for TOML string values."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def make_post(article):
    """
    Write a Hugo markdown post file for the given article.
    Returns the path of the created file.
    """
    slug = slug_from_url(article["url"])
    date = article["date"]
    filename = f"{date}-{slug}.es-cl.md"
    filepath = os.path.join(POSTS_DIR, filename)

    title_escaped = escape_toml_string(article["title"])

    content = f"""+++
title = "{title_escaped}"
author = "Javier Sajuria"
date = "{date}"
slug = "{slug}"
categories = ["Press", "Spanish"]
tags = ["La Tercera"]

+++

_Columna publicada en [La Tercera][1]_

{article['body']}

 [1]: {article['url']}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  Created: {filepath}")
    return filepath


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)

    existing_slugs = get_existing_slugs()
    print(f"Found {len(existing_slugs)} existing Spanish posts.")

    article_urls = get_author_page_articles()

    new_files = []
    skipped = 0

    for url in article_urls:
        slug = slug_from_url(url)

        if slug in existing_slugs:
            skipped += 1
            continue

        article = fetch_article(url)
        if article is None:
            print(f"  SKIPPING {url} (extraction failed)")
            continue

        filepath = make_post(article)
        new_files.append(filepath)
        existing_slugs.add(slug)

        # Be polite to the server
        time.sleep(1)

    print(f"\nDone. {len(new_files)} new post(s) created, {skipped} already existed.")

    if not new_files:
        print("No new posts — nothing to commit.")
        sys.exit(0)

    print("New files:")
    for f in new_files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
