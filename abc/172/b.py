# vim: fileencoding=utf-8


def main():
    s = input()
    t = input()
    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
