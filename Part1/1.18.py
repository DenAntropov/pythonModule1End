A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

sum_ = A ** 2 + B ** 2
kvsum_ = (A + B) ** 2

if sum_ >= kvsum_:
    print("Сумма квадратов A и B больше или меньше квадрата их суммы!")

else:
    print("Сумма квадратов A и B меньше квадрата их суммы!")