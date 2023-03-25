import datetime


def get_datetime_now():
    """获取当前日期和时间"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
