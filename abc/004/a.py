# vim: fileencoding=utf-8

import math


def main():
    n = int(input())
    pairs = []
    for i in range(n):
        x, y = map(int, input().split())
        pairs.append((x, y))
    max = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            p = pairs[i]
            q = pairs[j]
            d = math.sqrt(((p[0] - q[0]) ** 2) + ((p[1] - q[1]) ** 2))
            if max < d:
                max = d
    print(max)


if __name__ == "__main__":
    main()
