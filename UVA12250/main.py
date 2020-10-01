#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/1 上午 11:12
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

import sys


def solve():
    case = 0

    while True:
        line = input()

        if line == '#':
            sys.exit(0)
        else:
            case += 1

        if line == 'HELLO':
            print("Case " + str(case) + ": ENGLISH")
        elif line == 'HOLA':
            print("Case " + str(case) + ": SPANISH")
        elif line == 'HALLO':
            print("Case " + str(case) + ": GERMAN")
        elif line == 'BONJOUR':
            print("Case " + str(case) + ": FRENCH")
        elif line == 'CIAO':
            print("Case " + str(case) + ": ITALIAN")
        elif line == 'ZDRAVSTVUJTE':
            print("Case " + str(case) + ": RUSSIAN")
        else:
            print("Case " + str(case) + ": UNKNOWN")


if __name__ == '__main__':
    solve()
