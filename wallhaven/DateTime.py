import datetime


def get_datetime():
    """获取当前日期和时间"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def get_time():
    """获取当前时间"""
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")
