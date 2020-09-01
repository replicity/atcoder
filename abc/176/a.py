# vim: fileencoding=utf-8


def main():
    N, X, T = map(int, input().split())
    c = -(-N // X)
    print(T * c)


if __name__ == "__main__":
    main()
