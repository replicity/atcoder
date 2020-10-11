#!/usr/bin/env python3
import sys

# N番目の荷物までで、価値が0~sum(v)の場合それぞれにおいて価値以上の荷物をナップサックに入れた場合の最小の重さをもつdpテーブルを作る
def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    maxV = sum(v)
    dp = [[float('inf')] * (maxV+1) for i in range(N+1)]

    # 何番目の荷物か
    for i in range(1, N+1):
        # 重さ
        weight = w[i-1]
        value = v[i-1]
        for j in range(1, maxV+1):
            # 価値を満たせない場合
            if j - value > 0 and dp[i-1][j-value] == 0:
                break
            # 今回の価値以下で重さが今回以上の場合
            if j <= value and  dp[i-1][j] > weight:
                dp[i][j] = weight
            # 今回の荷持を使うべきか
            elif dp[i-1][j] > dp[i-1][max(0, (j - value))] + weight:
                dp[i][j] = dp[i-1][max(0, (j - value))] + weight
            else:
                # 荷物を使わない場合は前回と同じ重さで更新
                dp[i][j] = dp[i-1][j]

    # for idp in dp:
    #     print(idp)

    for i in range(maxV, 0, -1):
        if dp[N][i] <= W:
            print(i)
            break

    # print(dp[N][W])
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)

if __name__ == '__main__':
    main()
