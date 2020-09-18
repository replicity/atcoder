#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int):
    if N == 1:
        print(0)
        return
    if N == 2:
        print(2)
        return
    ans = (10 ** N) - ((9 ** N )* 2) + (8 ** N)
    print(ans % MOD)



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