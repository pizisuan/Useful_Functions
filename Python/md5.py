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
    生成给定字符串的MD5加密值
    :param input_str: 输入字符串
    :return: 加密值
    """

    m2 = hashlib.md5()
    m2.update(input_str.encode("utf-8"))
    return m2.hexdigest().upper()


if __name__ == "__main__":
    input_str = "深圳市软件产业基地"
    out_str = get_md5(input_str)
    print(out_str)
