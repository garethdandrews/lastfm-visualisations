import api_service as api
import ast

res = api.getWeeklyArtistChart('1609156800', '1609761600')

print(res)