n = int(input("Введите число: "))
list_ = list(range(10, n + 1))

for i in list_:
    if (n >= 10) and (i % 2 == 1) and (i % 5 == 0):
        print(i)
    else:
        print("Введенное число меньше 10")
