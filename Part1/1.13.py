number = int(input("Введите число N: "))

cond_1 = number % 4 == 0
cond_2 = number % 7 == 0

if cond_1 or cond_2:
    print("Число кратно 4 или 7!")
else:
    print("Число не кратно 4 или не кратно 7")