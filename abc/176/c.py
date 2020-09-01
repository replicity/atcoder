# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    max = 0
    total = 0
    for i in li:
        if max < i:
            max = i
            continue
        elif max == i:
            continue
        else:
            total += max - i
    print(total)


if __name__ == "__main__":
    main()
