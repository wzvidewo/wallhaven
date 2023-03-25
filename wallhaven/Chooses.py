def get_categorize():
    """获取类别"""
    # 主要分类，抓取网站分类功能待实现
    categories = ['latest', 'hot', 'toplist', 'random']

    length = len(categories)
    for index in range(length):
        print(f'{index + 1}：{categories[index]}')
    while 1:
        categorize = int(input('请输入要爬取页面的分类序号：'))

        if 0 < categorize <= length:
            categorize = categories[categorize - 1]
            print(f'\t已选择：{categorize}。')
            break

    return categorize


def get_page():
    """ 获取要抓取的页数"""
    while 1:
        pages = int(input('请输入要爬取的页数：'))
        if 0 < pages:
            print(f'\t已选择{pages}页。')
            break
    return pages
