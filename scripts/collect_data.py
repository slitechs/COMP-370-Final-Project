
import csv
import json
import time

from datetime import date, timedelta, datetime

import os
from dotenv import load_dotenv
from atproto import Client

load_dotenv()

BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

if not BLUESKY_HANDLE or not BLUESKY_APP_PASSWORD:
    raise ValueError("Missing Bluesky credentials in .env")

client = Client()
client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

print("Successfully authenticated with Bluesky!")


START_DATE = date(2026, 10, 16)
MAX_DAYS = 3
STOP_THRESHOLD = 600
PAGE_LIMIT = 100

MOVIES = [
    "You Can See Everything",
    "Whalefall",
    "Sense and Sensibility"
]


# Store each unique post once, keyed by its AT URI.
all_posts = {}

# Store daily collection statistics.
daily_stats = []


# ==================================================
# LOCAL RELEVANCE FILTER
# ==================================================

def is_relevant(text, movie):
    text_lower = text.lower()

    return (
        movie.lower() in text_lower
        and (
            "movie" in text_lower
            or "film" in text_lower
        )
    )

# ==================================================
# RAW POST DATA
# ==================================================

def raw_post_data(post):
    """Convert the Bluesky SDK model to its original JSON field structure."""
    if hasattr(post, "model_dump"):
        return post.model_dump(mode="json", by_alias=True)

    return post.dict(by_alias=True)

# ==================================================
# FETCH POSTS FOR ONE MOVIE ON ONE DAY
# ==================================================

def fetch_posts(movie, day):
    posts = []
    cursor = None
    seen_cursors = set()
    next_day = day + timedelta(days=1)

    while True:
        params = {
            "q": f'"{movie}"',
            "lang": "en",
            "sort": "latest",
            "since": day.isoformat() + "T00:00:00Z",
            "until": next_day.isoformat() + "T00:00:00Z",
            "limit": PAGE_LIMIT
        }

        if cursor:
            params["cursor"] = cursor

        response = client.app.bsky.feed.search_posts(params)

        for post in response.posts:
            record = post.record
            text = record.text or ""

            if not post.uri:
                continue

            if not is_relevant(text, movie):
                continue

            created_at = record.created_at

            if not created_at:
                continue

            timestamp = datetime.fromisoformat(
                created_at.replace("Z", "+00:00")
            )

            if timestamp.date() != day:
                continue

            langs = record.langs or []

            if langs and not any(
                lang.split("-")[0].lower() == "en"
                for lang in langs
            ):
                continue

            # Preserve the original Bluesky post structure.
            posts.append(raw_post_data(post))

        next_cursor = response.cursor

        if not next_cursor or next_cursor in seen_cursors:
            break

        seen_cursors.add(next_cursor)
        cursor = next_cursor

        time.sleep(0.2)

    return posts


# ==================================================
# SAVE DATA
# ==================================================

def save_data():

    # Save original Bluesky post objects without adding fields.
    with open(
        "bluesky_movies.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            list(all_posts.values()),
            f,
            ensure_ascii=False,
            indent=2
        )

    # Keep daily collection statistics.
    if daily_stats:

        with open(
            "bluesky_daily_counts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=daily_stats[0].keys()
            )

            writer.writeheader()
            writer.writerows(daily_stats)


# ==================================================
# MAIN COLLECTION LOOP
# ==================================================

def collect_data():

    for day_number in range(MAX_DAYS):

        current_day = START_DATE + timedelta(
            days=day_number
        )

        print("\n" + "=" * 55)
        print(f"COLLECTING: {current_day}")
        print("=" * 55)

        day_uris = set()
        movie_counts = {}

        for movie in MOVIES:

            print(f"\nSearching: {movie}")

            posts = fetch_posts(movie, current_day)

            movie_uris = set()

            for post in posts:

                uri = post["uri"]

                movie_uris.add(uri)
                day_uris.add(uri)

                # Store the original Bluesky post only once.
                if uri not in all_posts:
                    all_posts[uri] = post

            movie_counts[movie] = len(movie_uris)

            print(f"Qualifying posts: {len(movie_uris)}")

        # Cumulative unique post count.
        total = len(all_posts)

        print("\nDAILY SUMMARY")
        print(f"Date: {current_day}")
        print(f"New unique posts: {len(day_uris)}")
        print(f"Cumulative unique posts: {total}")

        for movie, count in movie_counts.items():
            print(f"{movie}: {count}")

        # Record daily statistics.
        stats = {
            "date": current_day.isoformat(),
            "new_unique_posts": len(day_uris),
            "cumulative_unique_posts": total
        }

        for movie, count in movie_counts.items():
            stats[movie] = count

        daily_stats.append(stats)

        # Save progress after every day.
        save_data()

        # Stop only when total is greater than 600.
        if total > STOP_THRESHOLD:

            print("\nSTOPPING: More than 600 unique posts collected.")
            break

    else:
        print(f"\nSTOPPING: Maximum {MAX_DAYS}-day period reached.")

    # Final summary.
    print("\n" + "=" * 55)
    print("FINAL RESULTS")
    print("=" * 55)

    print(f"Total unique posts: {len(all_posts)}")

    for movie in MOVIES:
        count = sum(
            1
            for post in all_posts.values()
            if movie.lower() in post["record"]["text"].lower()
        )

        print(f"{movie}: {count}")

    save_data()

    print("\nFiles saved:")
    print("- bluesky_movies.json")
    print("- bluesky_daily_counts.csv")


if __name__ == "__main__":
    collect_data()
