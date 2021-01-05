import config
import requests


def getWeeklyArtistChart(date_from, date_to):
    payload = {
        'user': 'garethdandrews',
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

    response = requests.get(url, headers=headers, params=payload)

    if response.status_code == 200:
        return response.content
    else:
        return {}


print(getWeeklyArtistChart('1609156800', '1609761600'))