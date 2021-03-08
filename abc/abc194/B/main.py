#!/usr/bin/env python3

def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    a = [i for i, v in enumerate(A) if v == min(A)]
    b = [i for i, v in enumerate(B) if v == min(B)]

    if len(a) == 1 and len(b) == 1 and a[0] == b[0]:
        ta = A[a[0]]
        tb = B[b[0]]
        ans = ta + tb
        for i in a:
            A[i] = float('inf')
        for i in b:
            B[i] = float('inf')
        ans = min(ans, min(min(A), min(B)))
        print(ans)
    else:
        print(max(min(A), min(B)))


if __name__ == '__main__':
    main()
