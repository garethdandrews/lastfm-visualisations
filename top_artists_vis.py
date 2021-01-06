import api_service as api

# res = api.getWeeklyArtistChart('1609156800', '1609761600')

# print(res)

from datetime import datetime
ts = int(1609156800)

print(datetime.fromtimestamp(ts))

res = api.user_get_top_artists('12month')
print(len(res['artist']))
print(res['artist'][0])