#!/usr/bin/env python3
import sys
import math


def solve(X: int):
    if X == 1:
        print(1)
        return

    ans = 1
    for i in range(2 ,32):
        for j in range(2, 32):
            n = i ** j
            if n > X:
                break
            elif n >= ans:
                ans = n
    print(ans)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()