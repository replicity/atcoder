# vim: fileencoding=utf-8


def main():
    red, green, blue = map(int, input().split())
    k = int(input())
    res = "No"
    for i in range(k):
        if blue <= green or blue <= red:
            blue *= 2
        elif green <= red:
            green *= 2
        if blue > green and green > red:
            res = "Yes"
            break
    print(res)


if __name__ == "__main__":
    main()
