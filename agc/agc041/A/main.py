#!/usr/bin/env python3
import sys


def solve(n: int, a: int, b: int):
    d = b-a

    if d % 2 == 0:
        print(d//2)
        return
    else:
        m = min(a-1,n-b)
        ans = m + 1 + ((d-1)// 2)
    print(ans)


    return


# generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: you use the default template now. you can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)

if __name__ == '__main__':
    main()
