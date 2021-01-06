import api_service

# find users top artist
res = api_service.user_get_top_artists()
top_artist = res['artist'][0]['name']

print("Top Artist: " + top_artist)

res = api_service.user_get_weekly_chart_list()

print(res)

from datetime import datetime
ts = int(res['chart'][0]['from'])
print(datetime.fromtimestamp(ts))