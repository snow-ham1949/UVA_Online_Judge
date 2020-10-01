#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/1 下午 01:01
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve(case):
    line = input()
    ans = -1
    speed = []
    for tmp in line.split():
        speed.append(int(tmp))

    for c_i in range(1, speed[0] + 1):
        if speed[c_i] > ans:
            ans = speed[c_i]

    print("Case {0}: {1}".format(case, ans))


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        solve(i)
