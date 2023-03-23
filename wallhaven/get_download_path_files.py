import os

"""获取下载路径里的文件对象"""


def get_download_path_files(download_path):
    # 如果目录不存在 创建目录
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return os.listdir(download_path)
