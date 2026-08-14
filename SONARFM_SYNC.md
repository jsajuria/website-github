# SonarFM YouTube Sync

Automates adding SonarFM Chile video appearances to the Hugo site as Posts.

---

## How it works

Two files are needed:

- **`.github/scripts/sync_sonarfm.py`** — fetches SonarFM Chile's YouTube RSS feed, filters for videos with "Sajuria" in the title, and creates Hugo markdown posts with an embedded YouTube player.
- **`.github/workflows/sync_sonarfm.yml`** — GitHub Actions workflow that runs the script every Thursday at 9am Chile time and commits any new posts back to the repo.

Each new video becomes two files in `exampleSite/content/posts/`:
- `YYYY-MM-DD-yt-VIDEO_ID.md`
- `YYYY-MM-DD-yt-VIDEO_ID.es-cl.md`

Posts use `categories = ["Media"]` and `tags = ["SonarFM", "Radio"]`, with the title prefixed `[VIDEO]`.

---

## Setup (one time)

### 1. Create the sync script

Create `.github/scripts/sync_sonarfm.py`:

```python
#!/usr/bin/env python3
"""
Syncs Javier Sajuria's SonarFM Chile radio appearances to the Hugo blog.
Fetches the channel RSS feed, finds videos mentioning Sajuria in the title,
and generates Hugo markdown files with an embedded YouTube video.

YouTube's public RSS feed returns the 15 most recent channel uploads — run this
at least as frequently as SonarFM publishes 15 videos (roughly weekly) so no
appearance is missed. For one-off backfills of older videos, run:
  python sync_sonarfm.py VIDEO_ID [VIDEO_ID ...]
"""

import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

import requests

CHANNEL_ID = "UC2WhQ76luTakpRSDWFTJ0YA"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
POSTS_DIR = "exampleSite/content/posts"
FILTER_TERM = "sajuria"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def get_existing_video_ids():
    ids = set()
    for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
        basename = os.path.basename(filepath)
        match = re.search(r"-yt-([A-Za-z0-9_-]{11})\.", basename)
        if match:
            ids.add(match.group(1))
    return ids


def fetch_rss():
    print(f"Fetching RSS feed: {RSS_URL}")
    resp = requests.get(RSS_URL, timeout=30)
    resp.raise_for_status()
    return ET.fromstring(resp.content)


def fetch_video_metadata(video_id):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    url = f"https://www.youtube.com/watch?v={video_id}"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()

    title_match = re.search(r'"title"\s*:\s*"([^"]+)"', resp.text)
    title = title_match.group(1) if title_match else f"SonarFM appearance ({video_id})"

    date_match = re.search(r'"publishDate"\s*:\s*"([^"]+)"', resp.text)
    if date_match:
        date_str = date_match.group(1)[:10]
    else:
        from datetime import date as dt
        date_str = dt.today().isoformat()

    return {"video_id": video_id, "title": title, "date": date_str}


def get_text(element, tag):
    el = element.find(tag, NS)
    return (el.text or "").strip() if el is not None else ""


def escape_toml(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def make_post(video_id, title, date_str):
    date = date_str[:10]
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    prefixed_title = f"[VIDEO] {title}"

    content = f"""+++
title = "{escape_toml(prefixed_title)}"
author = "Javier Sajuria"
date = "{date}"
slug = "yt-{video_id}"
categories = ["Media"]
tags = ["SonarFM", "Radio"]

+++

_Aparición en [Sonar Informativo, SonarFM Chile]({yt_url})_

{{{{< youtube {video_id} >}}}}
"""

    created = []
    for suffix in (f"{date}-yt-{video_id}.md", f"{date}-yt-{video_id}.es-cl.md"):
        path = os.path.join(POSTS_DIR, suffix)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created: {path}")
        created.append(path)

    return created


def sync_from_rss(existing_ids):
    root = fetch_rss()
    new_files = []
    skipped = 0

    for entry in root.findall("atom:entry", NS):
        title = get_text(entry, "atom:title")
        video_id = get_text(entry, "yt:videoId")
        published = get_text(entry, "atom:published")

        if FILTER_TERM not in title.lower():
            continue
        if video_id in existing_ids:
            skipped += 1
            continue

        print(f"New appearance: {title}")
        new_files.extend(make_post(video_id, title, published))
        existing_ids.add(video_id)

    print(f"RSS sync done: {len(new_files)} new file(s), {skipped} already existed.")
    return new_files


def backfill(video_ids, existing_ids):
    new_files = []
    for video_id in video_ids:
        if video_id in existing_ids:
            print(f"  Already synced: {video_id}")
            continue
        print(f"Fetching metadata for {video_id}...")
        try:
            meta = fetch_video_metadata(video_id)
        except Exception as e:
            print(f"  WARNING: Could not fetch {video_id}: {e}")
            continue
        print(f"  Title: {meta['title']}")
        new_files.extend(make_post(meta["video_id"], meta["title"], meta["date"]))
        existing_ids.add(video_id)
    return new_files


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    existing_ids = get_existing_video_ids()
    print(f"Found {len(existing_ids)} existing SonarFM post(s).")

    if len(sys.argv) > 1:
        new_files = backfill(sys.argv[1:], existing_ids)
    else:
        new_files = sync_from_rss(existing_ids)

    if not new_files:
        print("No new posts — nothing to commit.")
        sys.exit(0)

    print("New files:")
    for f in new_files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
```

### 2. Create the GitHub Actions workflow

Create `.github/workflows/sync_sonarfm.yml`:

```yaml
name: Sync SonarFM appearances

on:
  schedule:
    - cron: "0 12 * * 4"  # Every Thursday at 12pm UTC (9am Chile time)
  workflow_dispatch:       # Allows manual trigger from the GitHub Actions tab

jobs:
  sync:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install requests

      - name: Run SonarFM sync script
        run: python .github/scripts/sync_sonarfm.py

      - name: Commit and push new posts
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add exampleSite/content/posts/
          git diff --staged --quiet || git commit -m "Add new SonarFM appearance [automated]"
          git push
```

### 3. Commit and push

```bash
git add .github/scripts/sync_sonarfm.py .github/workflows/sync_sonarfm.yml
git commit -m "Add SonarFM YouTube sync"
git push
```

The workflow will appear in the **Actions** tab on GitHub. It runs automatically every Thursday, or can be triggered manually from that tab.

---

## Backfilling past videos

YouTube's RSS feed only returns the 15 most recent channel uploads. For older appearances, use one of these methods.

### Method A — Manual (simplest)

Browse the [SonarFM Chile channel](https://www.youtube.com/@SonarFMChile/videos), find past appearances, and copy the video ID from each URL (the part after `?v=`). Then run locally:

```bash
python .github/scripts/sync_sonarfm.py VIDEO_ID_1 VIDEO_ID_2 VIDEO_ID_3
```

Commit and push the resulting files:

```bash
git add exampleSite/content/posts/
git commit -m "Backfill SonarFM past appearances"
git push
```

### Method B — YouTube Data API (finds all videos automatically)

Use this when there are many past videos and you don't want to find them by hand.

**1. Get a free API key**

- Go to [console.cloud.google.com](https://console.cloud.google.com)
- Create or select a project
- Go to **APIs & Services → Library**, enable **YouTube Data API v3**
- Go to **APIs & Services → Credentials**, click **Create Credentials → API key**

**2. Search the channel for all Sajuria videos**

```bash
curl "https://www.googleapis.com/youtube/v3/search\
?channelId=UC2WhQ76luTakpRSDWFTJ0YA\
&q=Sajuria\
&type=video\
&maxResults=50\
&order=date\
&key=YOUR_API_KEY"
```

Each result includes a `videoId` under `items[].id.videoId`. If there are more than 50 results, repeat the request with `&pageToken=NEXT_PAGE_TOKEN` from the previous response.

**3. Pass the IDs to the backfill script**

```bash
python .github/scripts/sync_sonarfm.py ID_1 ID_2 ID_3 ...
```

Then commit and push as above.

---

## Reference

| Setting | Value | Where to change |
|---|---|---|
| Channel | SonarFM Chile | `CHANNEL_ID` in `sync_sonarfm.py` |
| Channel ID | `UC2WhQ76luTakpRSDWFTJ0YA` | `CHANNEL_ID` in `sync_sonarfm.py` |
| Filter keyword | `sajuria` (case-insensitive) | `FILTER_TERM` in `sync_sonarfm.py` |
| Schedule | Every Thursday 09:00 Chile | `cron` line in `sync_sonarfm.yml` |
| Post category | `Media` | `make_post()` in `sync_sonarfm.py` |
| Post tags | `SonarFM`, `Radio` | `make_post()` in `sync_sonarfm.py` |
