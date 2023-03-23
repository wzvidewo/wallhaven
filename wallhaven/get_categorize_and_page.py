"""获取类别和页数"""


def get_categorize_and_page():
    # 主要分类，抓取网站分类功能待实现
    categories = ['latest', 'hot', 'toplist', 'random']
    index = 1
    for category in categories:
        print(f'{index}：{category}')
        index += 1
    while 1:
        categorize = int(input('请输入要爬取页面的分类序号：'))

        if 0 < categorize <= len(categories):
            categorize = categories[categorize - 1]
            print(f'已选择：{categorize}')
        else:
            print('请选择正确的序号！')
        pages = int(input('请输入要爬取的页数：'))
        if 0 < pages:
            print(f'已选择{pages}页')
            break
    return [categorize, pages]
