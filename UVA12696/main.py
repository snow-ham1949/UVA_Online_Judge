#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/25 下午 01:29
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    n = int(input())

    ans = 0
    for i in range(n):
        length, width, depth, weight = list(map(float, input().split()))
        if weight > 7.0:
            print("0")
        else:
            if length <= 56.0 and width <= 45.0 and depth <= 25.0:
                print("1")
                ans += 1
            elif (length + width + depth) <= 125.0:
                print("1")
                ans += 1
            else:
                print("0")

    print(str(ans))
    

if __name__ == '__main__':
    solve()
