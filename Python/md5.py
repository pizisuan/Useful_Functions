"""
本模块用于生成给的字符串的MD5值

@author: Pizisuan
@date: 2019/09/18
@function: generate_md5

"""

__author__ = "Pizisuan"


import hashlib


def generate_md5(input_str):
    """
    根据地址获取id值-----MD5加密算法
    :param address: 输入地址
    :return: id值
    """

    m2 = hashlib.md5()
    m2.update(input_str.encode("utf-8"))
    return m2.hexdigest().upper()


if __name__ == "__main__":
    address = "深圳市软件产业基地"
    md5 = get_md5(address)
    print(md5)
