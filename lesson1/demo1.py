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


if __name__ == '__main__':
    print sigmod(1)
