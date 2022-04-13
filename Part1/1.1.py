number = int(input("Введите число для проверки на кратность 2 или 3: "))

cond_1 = number % 2 == 0
cond_2 = number % 3 == 0
if cond_1 or cond_2:
    print("Число кратно 2 или 3")
else:
    print("Число не кратно ни 2 ни 3!")
