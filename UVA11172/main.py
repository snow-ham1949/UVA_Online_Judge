def solve():
    line = input()
    num1, num2 = [int(tmp) for tmp in line.split()]

    if num1 == num2:
        print("=")
    elif num1 > num2:
        print(">")
    else:
        print("<")


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        solve()
