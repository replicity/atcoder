# vim: fileencoding=utf-8


def main():
    a = int(input())
    m = int(a / 1000)
    n = int(a % 1000)
    if n != 0:
        m += 1
    print(int((m * 1000) - a))


if __name__ == "__main__":
    main()
