# vim: fileencoding=utf-8


def main():
    n = int(input())
    string_list = [input() for i in range(n)]
    c1, c2, c3, c4 = 0, 0, 0, 0
    for s in string_list:
        if s == "AC":
            c1 += 1
        elif s == "WA":
            c2 += 1
        elif s == "TLE":
            c3 += 1
        elif s == "RE":
            c4 += 1
    print(f"AC x {c1}")
    print(f"WA x {c2}")
    print(f"TLE x {c3}")
    print(f"RE x {c4}")


if __name__ == "__main__":
    main()
