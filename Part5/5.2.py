def solution(n, y, x):
    for i in range(1, x + 1):
        if i == 1:
            result = n
            print("За {} день пробежали {} километров, всего с начала отсчета пробежали {} километров"
                  .format(i, ("%.2f" % n), ("%.2f" % result)))
        else:
            n += n * (y / 100)
            result += n
            print("За {} день пробежали {} километров, всего с начала отсчета пробежали {} километров"
                  .format(i, ("%.2f" % n), ("%.2f" % result)))


if __name__ == '__main__':
    n = int(input("Введите сколько пробежали км в первый день: "))
    y = int(input("Введите ежедневный % прибавки к норме пробежки: "))
    x = int(input("Введите сколько всего дней бежали: "))
    solution(n, y, x)