#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/18 上午 11:39
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

import sys


def solve():
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break

        while n >= 10:
            n = n // 10 + n % 10

        print(str(n))


if __name__ == '__main__':
    solve()
