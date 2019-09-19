"""
本模块用于文件基本操作

@author: Pizisuan
@date: 2019/09/19
@function: create_dir, view_tree, copy_file, rename_file, delete_file

"""

__author__ = "Pizisuan"


import os
import shutil


def create_dir(src_dir):
    '''
    创建目录
    :param src_dir: 目录路径
    :return:
    '''

    src_dir = src_dir.strip()
    src_dir = src_dir.rstrip("\\")

    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
        print("创建成功")
        return True
    else:
        print("目录已存在")
        return False


def view_tree(src_dir, n = 0):
    """
    打印指定文件夹的目录树
    :param src_dir: 目录路径
    :return:
    """
    src_dir = src_dir.strip()
    src_dir = src_dir.rstrip("\\")

    if os.path.exists(src_dir):
        for i in os.listdir(src_dir):
            p = os.path.join(src_dir,i)
            print (n * "|   " + "|__" + os.path.basename(p))
            if os.path.isdir(p):
                view_tree(p, n + 1)
    else:
        print("目录不存在")


def copy_file(src_file, des_dir, des_file_name=""):
    '''
    复制文件
    :param src_file:原始文件
    :param des_dir: 目标目录
    :param des_file_name: 目标文件名
    :return:
    '''

    if src_file is not None and os.path.exists(src_file):
        if des_file_name is None or des_file_name == "":
            des_file_name = os.path.split(src_file)[-1]
        shutil.copyfile(src_file, os.path.join(des_dir,des_file_name))
        print("复制成功")
        return True
    else:
        print("原文件不存在")
        return False


def rename_file(src_file, dest_file):
    '''
    重命名
    :param src_dir: 原始文件
    :param dest_file: 重命名文件
    :return:
    '''
    if os.path.exists(src_file):
        os.rename(src_file, dest_file)
        print("重命名成功")
        return True
    else:
        print("文件不存在")
        return False


def delete_file(src_file):
    '''
    删除文件
    :param src_file: 文件名
    :return:
    '''
    if os.path.exists(src_file):
        os.remove(src_file)
        print("删除成功")
        return True
    else:
        print("文件不存在")
        return False


if __name__ == "__main__":
    # 创建目录
    create_dir("E:\\FILM\\")

    # 查看目录树
    view_tree("./")

    # 复制文件
    copy_file("E:\\a.json","E:\\FILM\\", "b.json")

    # 重命名
    rename_file("E:\\a.json","E:\\b.json")

    # 删除文件
    delete_file("E:\\a.json")
