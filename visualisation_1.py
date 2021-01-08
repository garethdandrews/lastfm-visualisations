import api_service
from helper import unix_to_datetime
import pandas as pd

# find users top artist
top_artists = api_service.user_get_top_artists('overall')
top_artist = top_artists['artist'][0]['name']

print("Top Artist: " + top_artist)


# get user info
info = api_service.user_get_info()
registered = info['registered']['unixtime']
print("Registered(datetime): " + str(unix_to_datetime(registered)))


# find the week the user registered
weekly_chart_list = api_service.user_get_weekly_chart_list()

user_registered = False
registered = int(registered)
for n, week in enumerate(weekly_chart_list['chart']):
    if registered  >= int(week['from']) and registered <= int(week['to']):
        user_registered = True
        
    if user_registered:
        # look at weekly artist charts


registered_week = weekly_chart_list['chart'][n]

print(registered_week)
print(str(unix_to_datetime(registered_week['from'])))

weekly_artist_chart = api_service.user_get_weekly_artist_chart(registered_week)
print(weekly_artist_chart)

df = pd.DataFrame(columns=['week_from',top_artist])
df.loc[0] = [str(unix_to_datetime(week['from'])), 1000]

print(df.head())