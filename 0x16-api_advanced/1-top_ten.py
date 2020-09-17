#!/usr/bin/python3
''' Python script to extract top ten titles from subreddit '''

import requests


def top_ten(subreddit):
    ''' prints the titles of the first 10 hot posts listed for a given
    subreddit '''
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101\
    Firefox/80.0'
    headers = {
        'User-Agent': ua,
    }
    url = 'https://www.reddit.com/r/{}/hot/.json?=10'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        children = response.json().get('data').get('children')
        for idx, i in enumerate(children):
            if idx < 10:
                print(i.get('data').get('title'))
    else:
        print(None)
