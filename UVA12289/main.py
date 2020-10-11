#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/11 下午 05:01
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    value = str(input())
    n = len(value)
    one = "one"

    if n == 5:
        print("3")
    else:
        error_1 = 0
        for i in range(3):
            if value[i] != one[i]:
                error_1 += 1

        if error_1 <= 1:
            print("1")
        else:
            print("2")


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        solve()
