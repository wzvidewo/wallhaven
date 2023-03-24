import re
from subprocess import call

from bs4 import BeautifulSoup

import get_categorize
import get_image_url
import get_page
import get_response
import write_log

# idm程序路径
idm_path = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'

# 图片下载路径
download_path = r'C:\Documents\Wallhaven'

# 已下载图片链接存储文件路径
urls_path = r'logs\urls.txt'

# 获取 urlpath 文件中的链接去掉换行符存于列表 urls_lists 中
with open(urls_path, 'r') as f:
    urls_lists = f.read().split('\n')

categorize = get_categorize.get_categorize()
pages = get_page.get_page()

count = 1
for page in range(pages):
    response = get_response.get_response(f'https://wallhaven.cc/{categorize}?page={page + 1}')
    # 响应为空则是 get_response 捕获到了异常
    if response is None:
        print('请检查网络了连接!')
        exit(0)
    html = BeautifulSoup(response.text, 'lxml')
    # previews = html.find_all('a', class_='preview')
    previews = html.find_all('a', {'class': 'preview', 'target': '_blank'})
    for preview in previews:
        href = preview.get('href')

        # 判断指向图片真实地址的URL是否在列表 urls_lists 中，是就跳过这次请求
        if href in urls_lists:
            print(f'\t{count}：{href}：链接已存在')
            count += 1
            continue
        
        write_log.write_log(urls_path, href)
        image_url = get_image_url.get_image_url(href)
        # get_image_url会返回None
        if image_url is not None:
            file_name = re.search(r'wallhaven-(.+)(png|jpg)', image_url).group()
            # 把图片链接添加进IDM任务队列，但不开始
            call([idm_path, '/d', image_url, '/p', download_path, '/f', file_name, '/n', '/a'])
            print(f'\t{count}：{file_name}：已添加')
            count += 1

print('开始队列')
call([idm_path, '/s'])
