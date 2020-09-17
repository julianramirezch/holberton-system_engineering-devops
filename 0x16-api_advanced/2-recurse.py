#!/usr/bin/python3
''' recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.'''

import requests


def recurse(subreddit, hot_list=[], after=''):
    ''' returns a list containing the titles of all hot articles'''
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101\
    Firefox/80.0'
    headers = {
        'User-Agent': ua,
    }
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        children = response.json().get('data').get('children')
        [hot_list.append(i.get('data').get('title')) for i in children]
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)
