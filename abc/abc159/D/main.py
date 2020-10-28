#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    bucket = [0] * N

    # 各数値が何個あるか数える
    for i in A:
        bucket[i-1] += 1


    # すべてのボールを使えた場合の場合の数を組み合わせを求める
    total = 0
    for i in range(N):
        num = bucket[i]
        if num > 2:
            total += (num * (num -1)) // 2
        elif num == 2:
            total += 1

    # n番目のボールを除いた場合の数を求める
    for i in A:
        ans = total
        num = bucket[i-1]
        t = 0
        if num > 3:
            t = ((num * (num -1)) // 2)  - (((num -1) * (num -2)) // 2)
        elif num == 3:
            t = 2
        elif num == 2:
            t = 1
        print(ans - t)


    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)

if __name__ == '__main__':
    main()
