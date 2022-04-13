number = int(input("Введите число для проверки: "))

cond_1 = number % 3 != 0
cond_2 = number % 7 == 0
cond_3 = number % 10 == 0

if cond_1 and cond_2 and cond_3:
    print("Число удовлетворяет всем условиям!")
else:
    print("Число не удовлетворяет одному из условий!")