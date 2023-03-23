import os
import re

"""向指定路径的文件写入指定的信息"""

path = r'logs\logs.txt'


def write_log(log):
    # 使用正则表达式匹配任意字符，直到遇到最后一个斜杠或反斜杠为止。
    filepath = re.search(r'(.+)(/|(\\))', path).group()

    # 检查路径是否存在
    if not os.path.exists(filepath):
        os.makedirs(filepath)  # 创建路径
        open(path, 'w').close()  # 创建文件

    # 以附加模式写入文件，指定编码为utf-8（Win10的Pycharm中是GBK）
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'{log}\n')
