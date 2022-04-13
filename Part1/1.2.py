number_A = int(input("Введите число A для проверки на нечетность: "))
number_B = int(input("Введите число B для проверки на нечетность: "))

cond_A = number_A % 2 == 1
cond_B = number_B % 2 == 1
if cond_A and cond_B:
    print("Числа A и B нечетные")
else:
    print("Одно из чисел четное!")