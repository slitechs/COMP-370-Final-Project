from dotenv import load_dotenv
from atproto import Client
import os

load_dotenv()

client = Client()
client.login(
    os.getenv("BLUESKY_HANDLE"),
    os.getenv("BLUESKY_APP_PASSWORD")
)

response = client.app.bsky.feed.search_posts({
    "q": '"Whalefall"',
    "lang": "en",
    "limit": 5
})

print("Posts returned:", len(response.posts))

for post in response.posts:
    print(post.record.text)