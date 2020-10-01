#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/1 上午 11:27
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    line = input()
    l, w, h = [int(tmp) for tmp in line.split()]

    if l > 20 or w > 20 or h > 20:
        return 0
    else:
        return 1


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        ans = solve()
        if ans == 1:
            print('Case %d: good' % i)
        else:
            print('Case %d: bad' % i)
