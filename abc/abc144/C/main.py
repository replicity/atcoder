#!/usr/bin/env python3
import sys
import math


def solve(N: int):
    ans = float('inf')

    for i in range(2, int(math.sqrt(N)+1)):
        s = N / i
        if s.is_integer():
            t = i + s -2
            ans = min(ans, t)
    if ans == float('inf'):
        ans = N -1
    print(int(ans))

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
