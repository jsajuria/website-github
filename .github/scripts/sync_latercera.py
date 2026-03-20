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


def html_to_markdown(html_text):
    """
    Convert a paragraph that may contain inline HTML (e.g. <a href="...">link</a>,
    <em>, <strong>) into clean markdown.
    """
    frag = BeautifulSoup(html_text, "html.parser")
    # Replace <a href="url">text</a> with [text](url)
    for a in frag.find_all("a", href=True):
        a.replace_with(f"[{a.get_text()}]({a['href']})")
    # Replace <strong>/<b> with **text**
    for tag in frag.find_all(["strong", "b"]):
        tag.replace_with(f"**{tag.get_text()}**")
    # Replace <em>/<i> with _text_
    for tag in frag.find_all(["em", "i"]):
        tag.replace_with(f"_{tag.get_text()}_")
    return frag.get_text()


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

    # Extract title and date from JSON-LD
    title = ""
    date = ""
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
            if isinstance(data, list):
                data = next((d for d in data if d.get("@type") == "NewsArticle"), None)
                if not data:
                    continue
            if data and data.get("@type") == "NewsArticle":
                title = data.get("headline", "").strip()
                date_raw = data.get("datePublished", "")
                date = date_raw[:10] if date_raw else ""
                if not re.match(r"\d{4}-\d{2}-\d{2}", date):
                    print(f"  WARNING: Unexpected date format '{date_raw}' for {url}")
                    date = ""
                break
        except (json.JSONDecodeError, AttributeError):
            continue

    if not title or not date:
        print(f"  WARNING: Could not extract title/date from {url}")
        return None

    # Extract paragraphs from Arc XP content_elements JSON (preserves paragraph breaks)
    body_md = ""
    for script in soup.find_all("script"):
        text = script.string or ""
        if "content_elements" not in text:
            continue
        # Find the JSON object containing content_elements
        match = re.search(r'\{[^{}]*"content_elements"\s*:\s*\[.*?\]\s*[,}]', text, re.DOTALL)
        if not match:
            # Try broader search for the fusion state / page data blob
            match = re.search(r'"content_elements"\s*:\s*(\[.*?\])\s*[,}]', text, re.DOTALL)
            if not match:
                continue
            elements = json.loads(match.group(1))
        else:
            try:
                elements = json.loads(match.group(0)).get("content_elements", [])
            except json.JSONDecodeError:
                inner = re.search(r'"content_elements"\s*:\s*(\[.*?\])\s*[,}]', text, re.DOTALL)
                if not inner:
                    continue
                elements = json.loads(inner.group(1))

        paragraphs = [
            html_to_markdown(el["content"].strip())
            for el in elements
            if el.get("type") == "text" and el.get("content", "").strip()
        ]
        if paragraphs:
            body_md = "\n\n".join(paragraphs)
            break

    # Fall back to HTML <p> tags inside the article element
    if not body_md:
        article_el = soup.find("article") or soup.find(class_=re.compile(r"article|story|body", re.I))
        if article_el:
            paragraphs = [p.get_text(strip=True) for p in article_el.find_all("p") if p.get_text(strip=True)]
            body_md = "\n\n".join(paragraphs)

    if not body_md:
        print(f"  WARNING: Could not extract body text from {url}")
        return None

    return {
        "title": title,
        "date": date,
        "body": body_md,
        "url": url,
    }


def escape_toml_string(s):
    """Escape double quotes and backslashes for TOML string values."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def make_post(article):
    """
    Write Hugo markdown post files for the given article.
    Creates both .md (English/default) and .es-cl.md (Spanish) so the
    post appears in both language versions of the site.
    Returns the list of paths created.
    """
    slug = slug_from_url(article["url"])
    date = article["date"]
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

    created = []
    for ext in (f"{date}-{slug}.md", f"{date}-{slug}.es-cl.md"):
        filepath = os.path.join(POSTS_DIR, ext)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created: {filepath}")
        created.append(filepath)

    return created


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

        new_files.extend(make_post(article))
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
