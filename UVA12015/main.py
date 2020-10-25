#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/25 下午 12:51
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    maxScore = -1
    urls = []
    for i in range(10):
        url, score = input().split()
        score = int(score)
        urls.append((url, score))
        maxScore = max(maxScore, score)

    for url, score in urls:
        if score == maxScore:
            print(url)


if __name__ == '__main__':
    n = int(input())
    for case in range(n):
        print("Case #{0}:".format(case + 1))
        solve()
