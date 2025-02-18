#!/usr/bin/python3
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://oauth.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    if response.status_code == 200:
        json = response.json()
        data = json["data"]["children"]
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
# top_ten("sudan")