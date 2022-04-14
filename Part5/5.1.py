def check(i):
    n = 0
    while i > 1:
        if i % 2 == 0:  # i = i // 2 if i % 2 == 0 else 3 * i + 1
            i = i // 2
        else:
            i = 3 * i + 1
        n += 1
    return n


def task():
    num1 = int(input("Введите нижнюю границу проверяемого диапазона: "))
    num2 = int(input("Введите верхнюю границу проверяемого диапазона: "))
    for k in range(num1, num2 + 1):
        print(k, check(k))


if __name__ == '__main__':
    task()