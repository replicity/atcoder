#!/usr/bin/env python3

def main():
    ans = 0
    H, W = map(int,input().split())
    m = [0] * H
    for i in range(H):
        m[i] = list(input())

    for i in range(H+1):
        for j in range(W):
            a = 0
            if i != H and m[i][j] == '#':
                a += 1
            if i != 0 and m[i-1][j] == '#':
                a += 1
            if i != H and j != 0 and m[i][j-1] == '#':
                 a += 1
            if i != 0 and j !=0 and m[i-1][j-1] == '#':
                a += 1
            if a == 3 or a == 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
