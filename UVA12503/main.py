#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/25 下午 01:02
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def solve():
    n = int(input())

    ans = 0
    action = []
    for i in range(n):
        cmd = input().strip()
        move = cmd.split()
        if len(move) == 1:
            act = move[0]
        else:
            act = action[int(move[2]) - 1]
        action.append(act)

        if act == 'LEFT':
            ans -= 1
        else:
            ans += 1

    print(str(ans))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
