#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/11 下午 05:11
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

import sys

def solve():
    for line in sys.stdin:
        a, b = [int(tmp) for tmp in line.split()]
        if a == -1 and b == -1:
            break

        if a > b:
            a, b = b, a

        ans = min(b - a, 99 - b + a + 1)

        print(ans)

if __name__ == '__main__':
    solve()
