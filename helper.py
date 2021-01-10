from datetime import datetime
import api_service

def unix_to_datetime(unix):
    return datetime.fromtimestamp(int(unix)).strftime('%d-%m-%Y')

def get_users_registered_week():
    info = api_service.user_get_info()
    return int(info['registered']['unixtime'])