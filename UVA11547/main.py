#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/26 下午 06:34
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        ans = 315 * n + 36962
        if ans > 0:
            print(((ans % 100) - (ans % 10)) // 10)
        else:
            print(((ans % 10) - (ans % 100)) // 10 + 9)


if __name__ == '__main__':
    solve()
