import random
import time

import requests
from fake_useragent import UserAgent
from requests import HTTPError
from requests.exceptions import SSLError, ProxyError, ConnectionError, ChunkedEncodingError

import get_datetime_now
import write_log

"""获取指定url的html代码"""


def get_response(url):
    response = None  # 局部变量 'response' 可能在赋值前引用
    sleep_time = random.randint(5, 10)  # 随机等待5到10秒，10到20秒(两个403错误）
    try:
        # 每次请求都随机生成User-Agent
        response = requests.get(url, headers={'User-Agent': str(UserAgent().random)})
        time.sleep(sleep_time)
        print(f'{url}：{response.status_code} 随机等待：{sleep_time} S')
    except HTTPError as e:
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} HTTP请求错误！{response.status_code} {e}')
    except SSLError as e:
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 证书不安全！{e}')
    except ProxyError as e:
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 代理服务器无法连接或响应超时！{e}')
    except ConnectionError as e:
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 网络连接失败或超时！{e}')
    except ChunkedEncodingError as e:
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 获取数据不完整！{e}')
    return response
