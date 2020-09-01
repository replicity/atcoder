# vim: fileencoding=utf-8


def main():
    s = input()
    t = input()
    lt = len(t)
    ans = lt
    for i in range(0, len(s) - lt + 1):
        sub = s[i : i + lt]
        c = 0
        for j in range(0, lt):
            if sub[j] != t[j]:
                c += 1
        if ans > c:
            ans = c
    print(ans)


if __name__ == "__main__":
    main()
