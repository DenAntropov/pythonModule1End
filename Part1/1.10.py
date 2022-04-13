number_A = int(input("Введите число А: "))
number_B = int(input("Введите число B: "))
number_C = int(input("Введите число C: "))
number_D = int(input("Введите число D: "))

cond_A = number_A % 2 == 0
cond_B = number_B % 2 == 0
cond_C = number_C % 2 == 0
cond_D = number_D % 2 == 0

if (cond_A and cond_B) or (cond_A and cond_C) or (cond_A and cond_D) or (cond_B and cond_C) or (cond_B and cond_D) or (cond_C and cond_D):
    print("Ровно два числа из четырех - четные!")
else:
    print("Больше или меньше двух чисел из списка четные/нечетные!")