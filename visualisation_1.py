import api_service
from helper import unix_to_datetime

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

registered = int(registered)
for week in weekly_chart_list['chart']:
    if registered  >= int(week['from']) and registered <= int(week['to']):
        break

print("From: " + str(unix_to_datetime(week['from'])))
print("To: " + str(unix_to_datetime(week['to'])))
