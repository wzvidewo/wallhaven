import re

from bs4 import BeautifulSoup

import Response


def get_image_url(image_url):
    """获取预览图片里面的真实图片链接"""
    response = Response.get_response(image_url)
    # 响应为空，则重新请求
    while response is None:
        response = Response.get_response(image_url)
    bs = BeautifulSoup(response.text, 'lxml')
    img = bs.find('img', id='wallpaper')
    src_url = re.search(r'https?://.+(png|jpg)', img.prettify()).group()
    return src_url

# img = bs.find('img', id='wallpaper', src=re.compile(r'https?://.+(png|jpg)'))
# src_url = img.get('src')  # 该方法有时会获取不到（属性src变成了data-cfsrc，原因：Cloudflare的图片防盗链功能)
