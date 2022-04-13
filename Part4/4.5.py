import random


def solution(a):
    mlist = [random.randint(-10, 10) for i in range(a)]
    print(mlist)
    m = 0
    n = 1
    for i in mlist:
        if i < 0:
            m += 1    # Количество отрицательных элементов
            n *= i  # Произведение отрицательных элементов
    print(m)
    print(n)
    k = 0
    for i in mlist:
        if i % 2 == 1:
            k += i
    print(k)    #Сумма нечетных элементов


if __name__ == '__main__':
    a = int(input("Введите длину списка случайных чисел: "))
    solution(a)
