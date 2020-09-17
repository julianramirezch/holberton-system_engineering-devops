#!/usr/bin/python3
'''  function that queries the Reddit API and returns the number of
subscribers '''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''  returns the number of subscribers '''
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101\
    Firefox/80.0'
    headers = {
        'User-Agent': ua,
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return (response.json().get('data').get('subscribers'))

    return 0
