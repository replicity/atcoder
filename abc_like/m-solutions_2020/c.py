# vim: fileencoding=utf-8


def main():
    n, k = map(int, input().split())
    aList = list(map(int, input().split()))
    hyoukaList = []
    c = 1
    for i in range(n):
        if i < k:
            continue
        b = aList[i - k]
        a = aList[i]

        if b < a:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
