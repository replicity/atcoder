#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    s = set()
    for t in S:
        s.add(t)
    for t in S:
        tt = "!" + t
        if t in s and tt in s:
            if t in s:
                if t[0] == "!":
                    print(t[1:])
                    return
            if tt in s:
                print(t)
                return

    print("satisfiable")

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()