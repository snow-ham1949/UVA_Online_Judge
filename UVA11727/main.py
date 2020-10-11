#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/11 下午 04:55
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve(case):
    salary = []
    line = input()
    for tmp in line.split():
        salary.append(int(tmp))

    salary.sort()

    print("Case {0}: {1}".format(case, salary[1]))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        solve(i + 1)
