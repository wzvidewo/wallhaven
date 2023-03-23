""" 获取要抓取的页数"""


def get_page():
    while 1:
        pages = int(input('请输入要爬取的页数：'))
        if 0 < pages:
            print(f'已选择{pages}页')
            break
    return pages
