import requests
from fake_useragent import UserAgent
from requests import HTTPError
from requests.exceptions import SSLError, ProxyError, ConnectionError

import get_datetime_now
import write_log

"""获取指定url的html代码"""


def get_response(url):
    response = None  # 局部变量 'response' 可能在赋值前引用
    try:
        # 每次请求都随机生成User-Agent
        response = requests.get(url, headers={'User-Agent': str(UserAgent().random)})
    except HTTPError as e:
        # 4xx（客户端错误）或5xx（服务器错误）
        # 检查URL是否正确 检查网络连接是否正常 检查代理设置是否正确 禁用代理（不推荐）
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} HTTP请求错误！{response.status_code} {e}')
        return None
    except SSLError as e:
        # 检查URL是否正确 检查网络连接是否正常 检查SSL证书是否过期或无效 禁用SSL证书验证（不推荐）
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 证书不安全！{e}')
        return None
    except ProxyError as e:
        # 检查代理服务器是否可用 检查网络连接是否正常 检查代理设置是否正确 禁用代理（不推荐）
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 代理服务器无法连接或响应超时！{e}')
        return None
    except ConnectionError as e:
        # 检查URL是否正确 检查网络连接是否正常 检查代理设置是否正确 禁用代理（不推荐）
        write_log.write_log(f'{get_datetime_now.get_datetime_now()} {url} 网络连接失败或超时！{e}')
        return None
    else:
        return response
