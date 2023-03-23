import datetime

"""获取当前日期和时间"""


def get_datetime_now():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
