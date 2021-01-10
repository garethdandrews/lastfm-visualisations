import api_service
from helper import unix_to_datetime, get_users_registered_week
import pandas as pd

df = pd.DataFrame(columns=['Week'])

registered = get_users_registered_week()
weekly_chart_list = api_service.user_get_weekly_chart_list()

i = 0
user_registered = False
for n, week in enumerate(weekly_chart_list['chart']):
    if registered  >= int(week['from']) and registered <= int(week['to']):
        user_registered = True
        weekly_artist_chart = api_service.user_get_weekly_artist_chart(week)
        print(weekly_artist_chart)
        row = {}
        for artist in weekly_artist_chart['artist']:
            row[artist['name']] = artist['playcount']
        df.loc[i] = row
        i += 1
        print(row)
        break

print(df)