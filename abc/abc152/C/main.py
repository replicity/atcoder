#!/usr/bin/env python3
import sys


def solve(N: int, P: "List[int]"):
    ans = 1
    min = P[0]
    for i in range(1, N):
        if min > P[i]:
            ans += 1
            min = P[i]

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
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)

if __name__ == '__main__':
    main()