# vim: fileencoding=utf-8

MOD = (10 ** 9) + 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sums = [0] * N
    sums[N-1] = A[N-1]
    ans = 0
    for i in range(N-2, -1, -1):
        sums[i] += sums[i+1] + A[i]

    for i in range(N - 1):
        ans += (A[i] * sums[i+1]) % MOD
    print(ans% MOD)


if __name__ == "__main__":
    main()
