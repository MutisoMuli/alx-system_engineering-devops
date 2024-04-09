#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number
of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: Number of subscribers of the subreddit, or 0 if invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Chrome/99.0.9999.999 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            return response.json().get('data').get('subscribers')
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name: ")
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"Number of subscribers in {subreddit_name}: {subscribers_count}")
