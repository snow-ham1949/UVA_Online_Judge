def solve():
    n = int(input())
    L = 0
    R = 1000000000000000000

    while L < R:
        M = (L + R + 1) // 2
        if M * (M + 1) // 2 > n:
            R = M - 1
        else:
            L = M

    print(L)


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        solve()
