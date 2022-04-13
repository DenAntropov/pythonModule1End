number = int(input("Введите число для проверки: "))

cond_1 = number % 2 == 0
cond_2 = number % 7 == 0
cond_3 = number % 11 != 0
cond_4 = number % 13 != 0

if cond_1 and cond_2 and cond_3 and cond_4:
    print("Число удовлетворяет всем условиям!")
else:
    print("Число не удовлетворяет одному из условий!")
