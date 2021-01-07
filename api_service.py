import config
import requests
import json
from time import sleep

def user_get_info():
    return get({
        'method': 'user.getInfo'
    })


def user_get_top_artists(period):
    return get({
        'period': period,
        'method': 'user.getTopArtists'
    })


def user_get_weekly_chart_list():
    return get({
        'method': 'user.getWeeklyChartList'
    })


def user_get_weekly_artist_chart(week):
    return get({
        'from': week['from'],
        'to': week['to'],
        'method': 'user.getWeeklyArtistChart'
    })


def get(payload):
    headers = {'User-Agent': config.USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['user'] = config.USER
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

