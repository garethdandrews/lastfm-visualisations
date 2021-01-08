from datetime import datetime

def unix_to_datetime(unix):
    return datetime.fromtimestamp(int(unix)).strftime('%d-%m-%Y')