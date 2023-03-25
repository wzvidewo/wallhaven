import Files

"""向指定路径的文件写入指定的信息"""


def write_log(path, log):
    Files.create(path)

    # 以附加模式写入文件，指定编码为utf-8（Win10的Pycharm中是GBK）
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'{log}\n')
