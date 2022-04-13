number = int(input("Введите число N: "))

cond_1 = number % 5 == 0
cond_2 = number % 10 == 0

if cond_1 and cond_2:
    print("Число кратно 5 и оканчивается нулем!")
else:
    print("Число не кратно 5 или не оканчивается 0!")