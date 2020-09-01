# vim: fileencoding=utf-8


def main():
    k = int(input().split()[2])
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    r = 0
    while True:
        read = 0
        if len(a) != 0 and len(b) != 0:
            ai = a.index(min(a))
            bi = b.index(min(b))
            if sum(a[: ai + 1]) < sum(b[: bi + 1]):
                read = a[0]
                a = a[1:]
            else:
                read = b[0]
                b = b[1:]
        elif len(a) == 0:
            read = b[0]
            b = b[1:]
        elif len(b) == 0:
            read = a[0]
            a = a[1:]
        else:
            break
        k -= read
        if k < 0:
            break
        r += 1
        if k == 0:
            break
    print(r)


if __name__ == "__main__":
    main()
