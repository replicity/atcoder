# vim: fileencoding=utf-8


def main():
    a, b, c, x, y = map(int, input().split())
    ans = float("inf")
    for i in range(0, max(x, y) * 2 + 1, 2):
        p = x - i // 2
        p = max(0, p)
        q = y - i // 2
        q = max(0, q)
        sum = a * p + b * q + c * i
        if ans > sum:
            ans = sum
    print(ans)


if __name__ == "__main__":
    main()
