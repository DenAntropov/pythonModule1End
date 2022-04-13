import random


def solution(a):
    mlist = set()
    while len(mlist) != a:
        mlist.add(random.randint(1, 100))
    print(mlist)


if __name__ == '__main__':
    a = int(input("Введите длину списка случайных чисел : "))
    solution(a)