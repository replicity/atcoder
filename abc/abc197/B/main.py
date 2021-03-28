#!/usr/bin/env python3


def main():
    H,W,X,Y = map(int, input().split())
    m = [[0] * W for i in range(H)]
    for i in range(H):
        m[i] = list(input())

    X = X - 1
    Y = Y - 1
    if m[X][Y] == "#":
        print(0)
        return

    ans = 1
    for i in range(X+1,H):
        if m[i][Y] == ".":
            ans += 1
        else:
            break

    for i in range(X-1,-1, -1):
        if m[i][Y] == ".":
            ans += 1
        else:
            break

    for i in range(Y+1,W):
        if m[X][i] == ".":
            ans += 1
        else:
            break

    for i in range(Y-1,-1, -1):
        if m[X][i] == ".":
            ans += 1
        else:
            break
    print(ans)
    return


if __name__ == '__main__':
    main()
