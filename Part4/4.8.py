import random


def solution(a):
    mlist = [random.randint(-100, 100) for i in range(a)]
    print(mlist)

    for i in range(len(mlist)):
        if mlist[i] % 10 == 4:
            mlist[i] = mlist[i] // 2
    print(mlist)


if __name__ == '__main__':
    a = int(input("Введите длину списка случайных чисел: "))
    solution(a)
