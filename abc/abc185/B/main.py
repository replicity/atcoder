#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N,M,T = map(int,input().split())
    t = 0
    n = N
    for i in range(M):
        A,B = map(int,input().split())
        r = B - A
        n -= (A - t)
        if n <= 0:
            print(NO)
            return
        n = min(N, n + r)
        t = B
    n -= (T - t)

    if n <= 0:
        print(NO)
    else:
        print(YES)
    return


if __name__ == '__main__':
    main()
