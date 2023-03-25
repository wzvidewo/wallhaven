import os
import re


def get_files(download_path):
    """获取下载路径里的文件对象"""
    # 如果目录不存在 创建目录
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return os.listdir(download_path)


def create(path):
    """如果文件不存在则创建文件"""
    # 使用正则表达式匹配任意字符，直到遇到最后一个斜杠或反斜杠为止。
    filepath = re.search(r'(.+)(/|(\\))', path).group()
    # 如果文件或路径不存在
    if not os.path.exists(filepath):
        os.makedirs(filepath)  # 创建路径
        open(path, 'w').close()  # 创建文件
