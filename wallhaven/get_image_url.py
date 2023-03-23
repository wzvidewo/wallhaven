from bs4 import BeautifulSoup

import get_response

"""获取预览图片里面的真实图片链接"""


def get_image_url(image_url):
    response = get_response.get_response(image_url)
    bs = BeautifulSoup(response.text, 'lxml')
    preview_url = bs.find('img', id='wallpaper')
    image_url = preview_url.get('src')
    return image_url
