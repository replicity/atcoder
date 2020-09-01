# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    res = 0
    li = li + li
    li.sort()
    tmp = int(len(li) / 2)
    print(sum(li[-tmp:-1]))


if __name__ == "__main__":
    main()
