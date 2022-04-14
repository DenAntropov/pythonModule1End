def solution(n: int, m: int):
    list_ = range(n, m+1)

    while True:
        print(n)
        n += 1
        if n > m:
            break

# def solution(n: int, m: int):
#     list_ = range(n, m+1)
#     while n != 0 and m != 0:
#         for i in list_:
#             print(i)

if __name__ == '__main__':
    n = int(input("Введите нижнюю границу: "))
    m = int(input("Введите верхнюю границу: "))
    solution(n, m)