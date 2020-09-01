# vim: fileencoding=utf-8


def main():
    s = input()
    c = 0
    if s[0] == "1":
        c += 1
    if s[1] == "1":
        c += 1
    if s[2] == "1":
        c += 1
    print(c)


if __name__ == "__main__":
    main()
