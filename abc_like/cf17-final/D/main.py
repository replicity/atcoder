#!/usr/bin/env python3
import sys


def solve(N: int, H: "List[int]", P: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        H[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, H, P)

if __name__ == '__main__':
    main()
