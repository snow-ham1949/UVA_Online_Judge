#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/26 下午 05:19
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    t = int(input())
    for i in range(0, t):
        line = input()
        n, m = [int(tmp) for tmp in line.split()]

        print(((n - 3) // 3 + 1) * ((m - 3) // 3 + 1))


if __name__ == '__main__':
    solve()