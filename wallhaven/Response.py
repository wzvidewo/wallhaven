import random
import time

import requests
from fake_useragent import UserAgent
from requests.exceptions import SSLError, ProxyError

import Datetime
import Logs

# 日志路径
logs_path = r'logs\logs.txt'


def get_response(url):
    """获取指定url的响应"""
    sleep_time = random.randint(15, 20)  # 生成随机等待时间
    response = None
    status_code = None
    try:
        # 每次请求都随机生成User-Agent
        response = requests.get(url, headers={'User-Agent': str(UserAgent().random)})
        status_code = response.status_code
        print(f'{url}：{status_code} 随机等待：{sleep_time} S')
        time.sleep(sleep_time)  # 随机等待
    except SSLError as e:
        Logs.write_log(logs_path, f'{Datetime.get_datetime_now()} {url} {status_code} {e}')
    except ProxyError as e:
        Logs.write_log(logs_path, f'{Datetime.get_datetime_now()} {url} {status_code} {e}')
    if status_code == 200:
        return response
    else:
        Logs.write_log(logs_path, f'{Datetime.get_datetime_now()} {url} {status_code}')
        print(f'\t请求失败：{url}：{status_code} 准备重新请求')
        get_response(url)
