#!/usr/bin/env python3
import sys
import math


def solve(H: int, W: int):
    if H == 1 or W == 1:
        print(1)
        return
    ans = math.ceil(H / 2) * math.ceil(W / 2) + (H // 2) * (W // 2)
    return print(ans)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(H, W)

if __name__ == '__main__':
    main()
