number_A = int(input("Введите число А: "))
number_B = int(input("Введите число B: "))
number_C = int(input("Введите число C: "))
number_D = int(input("Введите число D: "))

cond_1 = number_A / number_B
cond_2 = number_C / number_D


if cond_1 > cond_2:
    print("Дробь A/B > C/D!")
elif cond_1 == cond_2:
    print("Дробь A/B = C/D!")
else:
    print("Дробь A/B < C/D!")
    