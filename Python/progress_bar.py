"""
本模块用于实现简单进度条

@author: Pizisuan
@date: 2019/10/9
@function: progress_bar

"""

__author__ = "Pizisuan"

import time


def progress_bar(num):
    """绘制长度为num的进度条"""

    j = "#"; k = "="; t = "|/-\\"; #s = " " * (num + 1)

    for i in range(0, num + 1):
        j += "#"; k += "="; s = ("=" * i) + (" " * (num - i))

        # 控制百分比
        print(int(i/num*100), end='%\r')
        #print('%.2f' % (i/num*100), end='%\r')
        #print('%.2f' % (i*100/num), end='%\r')

        # 控制进度条样式
        #print('complete percent:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), int((i/num)*100), end='%\r')
        #print(str(int(i/num*100)) + '% ' + j + '->', end='\r')
        #print(k + ">" + str(int(i/num*100)), end='%\r')
        #print("[%s]" % t[i%4], end='\r')
        #print("[%s][%s][%.2f" % (t[i%4], k, (i/num*100)), "%]", end='\r')
        print("[%s][%s][%.2f" % (t[i%4], s, (i/num*100)), "%]", end='\r')

        time.sleep(0.1)

    print()


if __name__ == "__main__":
    progress_bar(20)
