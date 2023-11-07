#!/usr/bin/python3
"""
Importing requests module
"""

from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    # Check if the subredit is none, Return 0
    if subreddit is None or subreddit is not isinstance(subreddit, str):
        print("None")

    # Identifiying the user agent
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # The params. which mean how many post we want to print
    params = {"limit": 10}

    # Identify the url
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Make the requesst
    response = get(url, headers=user_agent, params=params)

    # Convert the response intp json format
    jsonResponse = response.json()

    # Try to get top posts
    try:
        row = jsonResponse.get('data').get('children')
        for i in row:
            print(i.get('data').get('title'))
    # If you could't get it
    except:
        print("None")
