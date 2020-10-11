#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/7 下午 03:01
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

import sys

def solve():
    case = 0
    for line in sys.stdin:
        r, n = [int(tmp) for tmp in line.split()]
        if r == 0 and n == 0:
            break

        case += 1
        if r > 27 * n:
            print("Case {0}: impossible".format(case))
        elif r <= n:
            print("Case {0}: 0".format(case))
        else:
            if (r - n) % n == 0:
                print("Case {0}: {1}".format(case, int((r - n) // n)))
            else:
                print("Case {0}: {1}".format(case, int((r - n) // n) + 1))


if __name__ == '__main__':
    solve()
