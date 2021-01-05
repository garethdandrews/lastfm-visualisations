import config
import requests
import json

def getWeeklyChartList():
    payload = {
        'user': config.USER
    }
    return get(payload)


def getWeeklyArtistChart(date_from, date_to):
    payload = {
        'user': config.USER,
        'from': date_from,
        'to': date_to,
        'method': 'user.getWeeklyArtistChart'
    }
    return get(payload)


def get(payload):
    headers = {'User-Agent': config.USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = config.API_KEY
    payload['format'] = 'json'

    res = requests.get(url, headers=headers, params=payload)

    if res.status_code == 200:
        # convert the result bytes to a dictionary and remove the top level of the dictionary
        res_dict = json.loads(res.content.decode('utf-8'))
        return list(res_dict.values())[0]
    else:
        return {}

