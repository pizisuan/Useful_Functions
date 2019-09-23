"""
本模块用于将utf-8文件与gbk格式文件相互转换

@author: Pizisuan
@date: 2019/09/23
@function: utf2gbk, gbk2utf

"""

__author__ = "Pizisuan"


def utf2gbk(input_file, output_file):
    """
    utf-8文件格式转换为gbk格式
    :param input_file: 输入文件---utf-8格式
    :param output_file: 输出文件---gbk格式
    :return:
    """
    with open(output_file,"w",encoding="gbk",errors="ignore",newline="") as o:
        with open(input_file,"r",encoding="utf-8",errors="ignore") as f:
            header = next(f)
            o.write(header)
            for row, line in enumerate(f,1):
                if divmod(row, 10000)[-1] == 0:
                    print(row, "completed...")
                o.write(line)
    print("Done...")


def gbk2utf(input_file, output_file):
    """
    gbk文件格式转换为utf-8格式
    :param input_file: 输入文件---gbk格式
    :param output_file: 输出文件---utf-8格式
    :return:
    """
    with open(output_file,"w",encoding="utf-8",errors="ignore",newline="") as o:
        with open(input_file,"r",encoding="gbk",errors="ignore") as f:
            header = next(f)
            o.write(header)
            for row, line in enumerate(f,1):
                if divmod(row, 10000)[-1] == 0:
                    print(row, "completed...")
                o.write(line)
    print("Done...")


if __name__ == "__main__":
    utf2gbk("test_utf8.csv","test_gbk.csv")
    gbk2utf("test_gbk.csv","test_utf8.csv")
