import random
import time

import requests
from fake_useragent import UserAgent

import DateTime
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
        response = requests.get(url, timeout=20, headers={'User-Agent': str(UserAgent().random)})
    except requests.exceptions.SSLError as e:
        Logs.write_log(logs_path, f'{DateTime.get_datetime()} {url} {status_code} {e}')
    except requests.exceptions.ProxyError as e:
        Logs.write_log(logs_path, f'{DateTime.get_datetime()} {url} {status_code} {e}')
    except requests.exceptions.Timeout as e:
        Logs.write_log(logs_path, f'{DateTime.get_datetime()} {url} {status_code} {e}')
    except requests.exceptions.ConnectionError as e:
        Logs.write_log(logs_path, f'{DateTime.get_datetime()} {url} {status_code} {e}')
    else:
        status_code = response.status_code
        print(f'{url}：{status_code} 随机等待：{sleep_time}秒 {DateTime.get_time()}')
        time.sleep(sleep_time)  # 随机等待

    if status_code == 200:
        return response
    else:
        Logs.write_log(logs_path, f'{DateTime.get_datetime()} {url} {status_code}')
        print(f'{url}：{status_code} 请求失败：准备重新请求 {DateTime.get_time()}')
        return None
