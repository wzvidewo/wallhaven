import re

from bs4 import BeautifulSoup

import Response

# 日志路径
logs_path = r'logs\logs.txt'


def get_image_url(image_url):
    """获取预览图片里面的真实图片链接"""
    response = Response.get_response(image_url)
    # 响应为空，则重新请求
    while response is None:
        response = Response.get_response(image_url)
    bs = BeautifulSoup(response.text, 'lxml')
    img = bs.find('img', id='wallpaper')
    # src_url = img.get('src')  # 该方法会有获取不到的情况（属性src变成了data-cfsrc，原因未知)
    src_url = re.search(r'https?://.+(png|jpg)', img.prettify()).group()
    return src_url
