#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/1 上午 11:35
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve(case):
    wall = []
    num = int(input())
    height = input()
    for tmp in height.split():
        wall.append(int(tmp))

    high_jump = 0
    low_jump = 0

    for step in range(1, len(wall)):

        if wall[step] > wall[step - 1]:
            high_jump += 1
        if wall[step] < wall[step - 1]:
            low_jump += 1

    print("Case {0}: {1} {2}".format(case, high_jump, low_jump))


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        solve(i)
