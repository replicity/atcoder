#!/usr/bin/env python3
import sys
import operator

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N, W, ST):
    a = [0] * (((10 ** 5) * 2) + 2)
    d = [0] * (((10 ** 5) * 2) + 2)
    for i in ST:
        a[i[0]] += i[2]
        d[i[1]] += i[2]
    w = 0
    for i in range(((10 ** 5) * 2) + 2):
        w += a[i]
        w -= d[i]
        if w > W:
            print(NO)
            return
    print(YES)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, W = map(int,input().split())
    ST = []
    for i in range(N):
        ST.append(tuple(map(int, input().split())))
    solve(N, W, ST)

if __name__ == '__main__':
    main()
