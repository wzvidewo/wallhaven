"""获取类别"""


def get_categorize():
    # 主要分类，抓取网站分类功能待实现
    categories = ['latest', 'hot', 'toplist', 'random']
    length = len(categories)
    for index in range(length):
        print(f'{index + 1}：{categories[index]}')
    while 1:
        categorize = int(input('请输入要爬取页面的分类序号：'))

        if 0 < categorize <= length:
            categorize = categories[categorize - 1]
            print(f'已选择：{categorize}')
            break

    return categorize
