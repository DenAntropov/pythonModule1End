import random


def solution(a):
    mlist = [random.randint(-10, 10) for i in range(a)]
    print(mlist)

    n = min(mlist)
    m = max(mlist)

    n_idx = mlist.index(n)
    m_idx = mlist.index(m) + 1
    n_idx, m_idx = min(n_idx, m_idx), max(n_idx, m_idx)

    klist = mlist[0:n_idx] + mlist[n_idx:m_idx][::-1] + mlist[m_idx::]

    print(klist)


if __name__ == '__main__':
    a = int(input("Введите длину списка случайных чисел: "))
    solution(a)
