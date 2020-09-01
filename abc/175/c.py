# vim: fileencoding=utf-8

import math


def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    n = math.ceil(X / D)
    r = 0
    if n > K:
        r = X - (K * D)
    else:
        r = X - (n * D)
        k2 = K - n
        if k2 % 2 == 1:
            r += D
    print(abs(r))


if __name__ == "__main__":
    main()
