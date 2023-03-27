import re
from subprocess import call

from bs4 import BeautifulSoup

import Chooses
import DateTime
import Files
import Image
import Logs
import Response

# idm程序路径
idm_path = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'

# 图片下载路径
download_path = r'C:\Documents\Wallhaven'

# 已下载图片链接存储文件路径
urls_path = r'logs\urls.txt'

# 日志路径
logs_path = r'logs\logs.txt'

# 如果文件或路径不存在
Files.create(logs_path)

# 如果urls_path存在就获取 urls_path 文件中的链接去掉换行符存于列表 urls_lists 中
with open(urls_path, 'r') as f:
    urls_lists = f.read().split('\n')

categorize = Chooses.get_categorize()
pages = Chooses.get_page()

count = 1
for page in range(pages):
    page_url = f'https://wallhaven.cc/{categorize}?page={page + 1}'
    response = Response.get_response(page_url)
    # 响应为空，则重新请求
    while response is None:
        response = Response.get_response(page_url)
    html = BeautifulSoup(response.text, 'lxml')
    previews = html.find_all('a', {'class': 'preview', 'target': '_blank'})
    for preview in previews:
        href = preview.get('href')

        # 判断指向图片真实地址的URL是否在列表 urls_lists 中，是就跳过这次请求
        if href in urls_lists:
            print(f'\t{count}：{DateTime.get_datetime()} {href}：链接已存在')
            count += 1
            continue

        Logs.write_log(urls_path, href)
        image_url = Image.get_image_url(href)
        # 使用正则表达式从后面开始匹配(英文字符串.英文字符串)
        file_name = re.search(r'(\w+\.\w+)$', image_url).group()
        # 把图片链接添加进IDM任务队列，但不开始
        call([idm_path, '/d', image_url, '/p', download_path, '/f', file_name, '/n', '/a'])
        print(f'\t{count}：{DateTime.get_time()} {file_name}：下载中……')
        call([idm_path, '/s'])
        count += 1
