# vim: fileencoding=utf-8


def main():
    s = input()
    t = 0
    for i in s:
        t += int(i)
    if t % 9 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
