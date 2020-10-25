#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/24 下午 10:00
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    while True:
        b, n = list(map(int, input().split()))
        if b == 0 and n == 0:
            break

        reserve = list(map(int, input().split()))
        for _ in range(n):
            s, e, val = list(map(int, input().split()))
            reserve[s - 1] -= val
            reserve[e - 1] += val

        flag = True
        for i in range(b):
            if reserve[i] < 0:
                flag = False
                break

        if flag:
            print("S")
        else:
            print("N")


if __name__ == '__main__':
    solve()
