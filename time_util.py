from datetime import datetime
from datetime import timedelta
import time

def now(addMinutes=0):
    return datetime.now() + timedelta(minutes=int(addMinutes))

def get_today():
    return datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)

def delta_min(date1, date2):
    diff = date2 - date1
    min_sec = divmod(diff.days * 86400 + diff.seconds, 60) # (min,sec)
    return min_sec[0]

def ellapsed_min(date):
    return delta_min(date, now())

def get_last_week():
    return datetime.now() - timedelta(days=7)

def get_date_days_ago(days):
    return datetime.now() - timedelta(days=days)

def get_date_hours_ago(days):
    return datetime.now() - timedelta(hours=days)

def get_date_CET(date):
    if date is None: return None
    newdate = date  + timedelta(hours=2)
    return newdate

def get_date_CET_from_DDMMYY(dateString):
    date = datetime.strptime(dateString,'%d%m%y')
    return get_date_CET(date)

def get_date_string(date):
    newdate = get_date_CET(date)
    time_day = str(newdate).split(" ")
    time = time_day[1].split(".")[0]
    day = time_day[0]
    return day + " " + time

def get_time_string(date):
    newdate = get_date_CET(date)
    return str(newdate).split(" ")[1].split(".")[0]

def isTimeFormat(input):
    try:
        datetime.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

def getMinutes(input):
    t1 = datetime.strptime(input, '%H:%M')
    t2 = datetime.strptime('00:00', '%H:%M')
    return int((t1-t2).total_seconds()//60)