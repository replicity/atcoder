# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    a = b = li[0]
    for i in li:
        a = min(a, i)
        b = max(b, i)
    print(b - a)


if __name__ == "__main__":
    main()
