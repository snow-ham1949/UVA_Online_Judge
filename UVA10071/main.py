import sys

def solve():
    for line in sys.stdin:
        if not line:
            break
        v, t = [int(tmp) for (tmp) in line.split()]

        print(v * t * 2)

if __name__ == '__main__':
    solve()
