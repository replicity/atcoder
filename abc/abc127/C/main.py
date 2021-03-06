#!/usr/bin/env python3
import sys


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    min = L[0]
    max = R[0]
    for i in range(M):
        if L[i] > min:
            min = L[i]
        if R[i] < max:
            max = R[i]
    ans = 0
    for i in range(1, N+1):
        if min <= i <= max:
            ans += 1
    print(ans)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, L, R)

if __name__ == '__main__':
    main()
