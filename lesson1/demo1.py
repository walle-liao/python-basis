#!/usr/bin/python
# encoding: utf-8

"""
@author: liaozhicheng.cn@163.com
@date: 2016/7/24
"""

from math import exp


def sigmod(x):
    y = 1 / (1.0 + exp(-x))
    return y


# __name__ == '__main__' 表示只有当该文件作为主模块运行时，if 语句后面的代码才会运行
# 而如果该文件是通过 import 引入到其他模块中使用时，if 后面的语句并不会执行
# 通常可用来将一些内部测试代码放在 if 语句后面
if __name__ == '__main__':
    print sigmod(1)
