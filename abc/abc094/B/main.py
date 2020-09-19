#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: int, A: "List[int]"):
    ans = 0
    for i in range(X-1, 0, -1):
        if i in A:
            ans += 1
    c = 0
    for i in range(X+1, N):
        if i in A:
            c += 1
    if ans > c:
        ans = c
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
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X, A)

if __name__ == '__main__':
    main()
