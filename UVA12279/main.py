#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/1 下午 01:12
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    case = 0
    while True:
        n = int(input())
        if n == 0:
            break

        case += 1
        ans = 0
        line = input()
        for tmp in line.split():
            a = int(tmp)
            if a > 0:
                ans += 1
            else:
                ans -= 1

        print("Case {0}: {1}".format(case, ans))


if __name__ == '__main__':
    solve()
