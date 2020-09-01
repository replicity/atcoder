# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))

    money = 1000
    stock = 0
    for i in range(n):
        today = li[i]
        max = today
        min = today

        sell = False
        buy = False

        # 株を買う場合
        if money > 0 and money >= today:
            for j in range(i + 1, n):
                target = li[j]
                if today > target:
                    break
                if today < target:
                    buy = True
                    break
        if buy:
            c = int(money / today)
            stock += c
            money -= c * today
            continue

        # 株を売る場合
        if stock > 0:
            min = today
            max = today
            for j in range(i + 1, n):
                f = li[j]
                if today < f:
                    max = f
                    break
                if min > f:
                    min = f
            if max == today:
                sell = True
            else:
                tm = money + stock * today
                ts = int(tm / min)
                if ts > stock:
                    sell = True
            if sell:
                money += stock * today
                stock = 0

    print(money)


if __name__ == "__main__":
    main()
