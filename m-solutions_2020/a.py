# vim: fileencoding=utf-8


def main():
    a = int(input())
    if a <= 599:
        print(8)
    elif a <= 799:
        print(7)
    elif a <= 999:
        print(6)
    elif a <= 1199:
        print(5)
    elif a <= 1399:
        print(4)
    elif a <= 1599:
        print(3)
    elif a <= 1799:
        print(2)
    elif a <= 1999:
        print(1)


if __name__ == "__main__":
    main()
