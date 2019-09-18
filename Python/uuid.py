"""
本模块用于生成UUID值

@author: Pizisuan
@date: 2019/09/18
@function: generate_uuid

"""

__author__ = "Pizisuan"


import uuid


def generate_uuid():
    """
    生成UUID值
    :param:
    :return:
    """
    return str(uuid.uuid1()).upper().replace('-', '')


if __name__ == "__main__":
    uid = generate_id()
    print(uid)
