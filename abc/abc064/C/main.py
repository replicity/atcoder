#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    ans = set()
    f = 0
    for i in a:
        if i <= 399:
            ans.add(0)
        elif i <= 799:
            ans.add(1)
        elif i <= 1199:
            ans.add(2)
        elif i <= 1599:
            ans.add(3)
        elif i <= 1999:
            ans.add(4)
        elif i <= 2399:
            ans.add(5)
        elif i <= 2799:
            ans.add(6)
        elif i <= 3199:
            ans.add(7)
        else:
            f += 1
    print(f"{max(len(ans),1)} {len(ans)+f}")


    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
