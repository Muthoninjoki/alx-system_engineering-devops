#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[]):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
    else:
        return None

    return hot_list
