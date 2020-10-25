#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/25 下午 01:14
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    n = int(input())
    digits = []
    for i in range(5):
        line = input()
        digits.append(line)

    for i in range(0, 4 * n, 4):
        if digits[0][i + 2] == '.':
            print("1", end='')
        elif digits[3][i] == '*':
            print("2", end='')
        else:
            print("3", end='')

    print("")


if __name__ == '__main__':
    solve()
