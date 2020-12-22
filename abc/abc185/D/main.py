#!/usr/bin/env python3
import math

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    alst = list(map(int, input().split()))
    alst.sort()
    alst.append(N+1)

    white = []
    i = 1
    for m in alst:
        r = m - i
        i = m+1
        if r == 0:
            continue
        white.append(r)

    if len(white) == 0:
        print(0)
        return

    s = min(white)
    print(sum(map(lambda x: math.ceil(x/s), white)))


if __name__ == '__main__':
    main()

