# vim: fileencoding=utf-8


def main():
    n = input()
    li = list(map(int, input().split()))
    ans = 0
    for a in li[0::2]:
        if a % 2 == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
