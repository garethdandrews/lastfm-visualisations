import api_service as api

res = api.getWeeklyArtistChart('1609156800', '1609761600')

print(res)

from datetime import datetime
ts = int(1609156800)

print(datetime.fromtimestamp(ts))