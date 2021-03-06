#!/usr/bin/env python3
import sys


def solve(S: str):
    if S[0] != "A":
        print("WA")
        return
    i = -1
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    else:
        i = S.index("C")
    S = S[:i]  + S[i+1:]
    S = S[1:]
    if S.islower():
        print("AC")
        return
    print("WA")

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
