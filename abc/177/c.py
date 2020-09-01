# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    res = 0
    m = 1000000007
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += li[i] * li[j]
            if res > m:
                print(res % m)
                return

    print(res % m)


if __name__ == "__main__":
    main()
