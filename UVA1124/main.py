#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/26 下午 04:55
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

import sys


def solve():
    for line in sys.stdin:
        if not line:
            break

        print(line, end="")


if __name__ == '__main__':
    solve()
