import sys

len = {}

def count(i):

    if (i in len):
        return len[i]
    if (i == 1):
        return 1

    tmp = i
    if (i % 2 == 0):
        i = i // 2
    else:
        i = 3 * i + 1

    len[tmp] = count(i) + 1
    return len[tmp]

def solve():
    for line in sys.stdin:
        if not line:
            break
        num1, num2 = [int(tmp) for(tmp) in line.split()]

        ans = 0
        for i in range(min(num1, num2), max(num1, num2) + 1):
            ans = max(ans, count(i))

        print(num1, num2, ans)

if __name__ == '__main__':
    solve()


