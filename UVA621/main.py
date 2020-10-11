#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/10 下午 03:44
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    line = str(input())
    n = len(line)
    if line == '1' or line == '4' or line == '78':
        print("+")
    elif line[n-2] == '3' and line[n-1] == '5':
        print("-")
    elif line[0] == '9' and line[n-1] == '4':
        print("*")
    else:
        print("?")


if __name__ == '__main__':
    case = int(input())
    for i in range(case):
        solve()
