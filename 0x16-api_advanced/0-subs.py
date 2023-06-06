#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0


if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers: {subscribers}")
