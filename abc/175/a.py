# vim: fileencoding=utf-8


def main():
    s = list(input())
    c = 0
    p = "S"
    r = 0
    for e in s:
        if e == "R":
            c += 1
        if c > r:
            r = c
        if e == "S":
            c = 0
    print(r)


if __name__ == "__main__":
    main()
