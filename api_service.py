import config
import requests
import json
from time import sleep

def user_get_top_artists():
    return get({
        'user': config.USER,
        'period': 'overall',
        'limit': 10
    })


def user_get_weekly_chart_list():
    return get({
        'user': config.USER
    })


def user_get_weekly_artist_chart(date_from, date_to):
    return get({
        'user': config.USER,
        'from': date_from,
        'to': date_to,
        'method': 'user.getWeeklyArtistChart'
    })


def get(payload):
    headers = {'User-Agent': config.USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = config.API_KEY
    payload['format'] = 'json'

    res = requests.get(url, headers=headers, params=payload)
    sleep(0.25)

    if res.status_code == 200:
        # convert the result bytes to a dictionary and remove the top level of the dictionary
        res_dict = json.loads(res.content.decode('utf-8'))
        return list(res_dict.values())[0]
    else:
        return {}

