from bs4 import BeautifulSoup

import Response

# 日志路径
logs_path = r'logs\logs.txt'


def get_image_url(image_url):
    """获取预览图片里面的真实图片链接"""
    response = Response.get_response(image_url)
    # 请求失败给我重新请求
    if response is None:
        response = Response.get_response(image_url)
    bs = BeautifulSoup(response.text, 'lxml')
    preview_url = bs.find('img', id='wallpaper')
    image_url = preview_url.get('src')
    return image_url
