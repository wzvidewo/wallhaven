import re
from subprocess import call

from bs4 import BeautifulSoup

import get_categorize_and_page
import get_download_path_files
import get_image_url
import get_response

# idm程序路径
idm_path = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'

# 图片下载路径
download_path = r'C:\Documents\Wallhaven'

# 获取下载文件夹里包含的文件列表
files = get_download_path_files.get_download_path_files(download_path)
choose = get_categorize_and_page.get_categorize_and_page()[0]
pages = get_categorize_and_page.get_categorize_and_page()[1]

count = 1
for page in range(pages):
    response = get_response.get_response(f'https://wallhaven.cc/{choose}?page={page + 1}')
    html = BeautifulSoup(response.text, 'lxml')
    previews = html.find_all('a', class_='preview')
    for preview in previews:
        href = preview.get('href')
        image_url = get_image_url.get_image_url(href)
        print(f'{count}：{image_url}')
        file_name = re.search(r'wallhaven-\w+\.(png|jpg)', image_url).group()

        # 判断该文件是否已下载，如果已下载则跳出循环
        if file_name in files:
            print(f'{file_name}：已存在')
            continue
        # 把图片链接添加进IDM任务队列，但不开始
        call([idm_path, '/d', image_url, '/p', download_path, '/f', file_name, '/n', '/a'])
        count += 1

    print('开始队列')
    call([idm_path, '/s'])
