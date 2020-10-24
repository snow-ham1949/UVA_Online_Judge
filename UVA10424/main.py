#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/18 上午 11:11
# @Author : Li, Yun-Fang
# @File : main.py
# @Software: PyCharm

def value_calculate(name):
    n = len(name)
    value = 0
    for i in range(n):
        if name[i].isalpha():
            value += (ord(name[i].lower()) - ord('a')) + 1

    while value >= 10:
        value = value // 10 + value % 10

    # print("value: {0}".format(value))

    return value


def solve():
    while True:
        try:
            name_1 = str(input())
        except EOFError:
            break

        name_2 = str(input())

        name_1_value = value_calculate(name_1)
        name_2_value = value_calculate(name_2)

        ans = min(name_1_value, name_2_value) / max(name_1_value, name_2_value) * 100.0
        print("{:.2f} %".format(ans))


if __name__ == '__main__':
    solve()
