#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(R: int, C: int, N: int, r: "List[int]", c: "List[int]", a: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    r = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    a = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(R, C, N, r, c, a)

if __name__ == '__main__':
    main()
