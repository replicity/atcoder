#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    s = {1}
    i = 1
    c = 0
    while True:
        c += 1
        i = a[i-1]
        if i == 2:
            print(c)
            break
        if i in s:
            print(-1)
            break
        s.add(i)

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
