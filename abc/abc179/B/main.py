#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, D: "List[List[int]]"):
    f = False
    c = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            c += 1
            if c == 3:
                f = True
                break
        else:
            c = 0
    if f:
        print("Yes")
    else:
        print("No")

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(2)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, D)

if __name__ == '__main__':
    main()