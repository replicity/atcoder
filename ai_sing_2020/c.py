# vim: fileencoding=utf-8


def main():
    N = int(input())
    ans = [0] * N
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                t = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x - 1
                if t >= len(ans):
                    break
                ans[t] += 1

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
