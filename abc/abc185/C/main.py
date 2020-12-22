#!/usr/bin/env python3
import sys
import math


def solve(L: int):
    print(math.comb(L-1, 11))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    solve(L)

if __name__ == '__main__':
    main()
