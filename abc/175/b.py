# vim: fileencoding=utf-8


def main():
    N = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(N):
        li = l[i]
        for j in range(i + 1, N):
            lj = l[j]
            if li == lj:
                continue
            for k in range(j + 1, N):
                lk = l[k]
                if li == lk or lj == lk:
                    continue
                if li < lj + lk and lj < li + lk and lk < li + lj:
                    c += 1
    print(c)


if __name__ == "__main__":
    main()
