import api_service
from helper import unix_to_datetime
import pandas as pd

# find users top artist
top_artists = api_service.user_get_top_artists('overall')
top_artist = top_artists['artist'][0]['name']

df = pd.DataFrame(columns=['week_from',top_artist])

# find the week the user registered
info = api_service.user_get_info()
registered = int(info['registered']['unixtime'])
weekly_chart_list = api_service.user_get_weekly_chart_list()

i = 0
user_registered = False
for n, week in enumerate(weekly_chart_list['chart']):
    if registered  >= int(week['from']) and registered <= int(week['to']):
        user_registered = True
        
    if user_registered:
        weekly_artist_chart = api_service.user_get_weekly_artist_chart(week)
        top_artist_plays = next((artist['playcount'] for artist in weekly_artist_chart['artist'] if artist['name'] == top_artist), 0)
        df.loc[i] = [str(unix_to_datetime(week['from'])), top_artist_plays]
        i += 1

print(df.head())