def solve():
    flag = 0
    while True:
        try:
            line = input()
        except EOFError:
            break

        ans = []
        for i in line:
            if i == "\"":
                if flag % 2 == 0:
                    ans.append("``")
                    flag = flag + 1
                else:
                    ans.append("''")
                    flag = flag + 1
            else:
                ans.append(i)

        print("".join(ans))


if __name__ == '__main__':
    solve()
