#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/18 上午 11:33
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    n = int(input())
    score = []
    for tmp in range(n):
        score.append(int(input()))

    ans = -150006
    max_score = -150006
    for i in range(n):
        ans = max(max_score - score[i], ans)
        max_score = max(max_score, score[i])

    print(str(ans))


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        solve()
