#!/usr/bin/env python3
import sys


def solve(N: int, C: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    R = max(max(a), max(b))
    ans = 0
    T = dict()

    # 値段が変化する日付をkeyにして、どの程度値段か変化するかをvalueにするdictを作成する
    for i in range(N):
        s = a[i]
        e = b[i] + 1
        p = c[i]

        if s in T:
            v = T[s]
            v[0] += p
            T[s] = v
        else:
            T[s] = [p, 0]

        if e in T:
            v = T[e]
            v[1] += p
            T[e] = v
        else:
            T[e] = [0, p]

    # 変化日がkeyなのでkeyの昇順になるようにsort
    sortedT = sorted(T.items(), key=lambda x:x[0])

    # 変化日と期間がわかるので計算していく
    i = sortedT[0][0]
    p = sortedT[0][1][0]
    for j in range(1, len(sortedT)):
        v = sortedT[j]
        d = v[0]
        ans += (d - i) * min(p, C)
        i = d
        p += v[1][0] - v[1][1]
    print(ans)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, a, b, c)

if __name__ == '__main__':
    main()
