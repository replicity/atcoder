#!/usr/bin/env python3
import copy

def main():
    N, M, Q = map(int, input().split())

    # タプルの価値が降順で重さが昇順のリストを作る
    t = dict()
    for i in range(N):
        w, v = map(int, input().split())
        if v in t:
            t[v].append(w)
        else:
            t[v] = [w]
    t = sorted(t.items(), key=lambda x:x[0], reverse=True)
    b = []
    for d in t:
        v = d[0]
        d[1].sort(reverse=True)
        for w in d[1]:
            b.append((v, w))
    # print(b)

    X = list(map(int,input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        # 使えない箱を取り除く
        xa = X[0:L-1]
        xb = X[R:]
        x = xa + xb

        tb = copy.copy(b)
        # print(tb)

        # 小さい箱から使う
        x.sort()
        # print(x)
        ans = 0
        for j in x:
            for k in tb:
                # print(k)
                if k[1] <= j:
                    ans += k[0]
                    tb.remove(k)
                    break
        print(ans)

if __name__ == '__main__':
    main()
