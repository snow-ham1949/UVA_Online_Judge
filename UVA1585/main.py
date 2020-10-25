#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/24 下午 09:55
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    ans = str(input())
    n = len(ans)
    score = 0
    correct = 0
    for i in range(n):
        if ans[i] == 'O':
            correct += 1
            score += correct
        else:
            correct = 0

    print(str(score))


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        solve()
