number_A = int(input("Введите число А: "))
number_B = int(input("Введите число B: "))
number_C = int(input("Введите число C: "))

cond_A = number_A % 3 == 0
cond_B = number_B % 3 == 0
cond_C = number_C % 3 == 0

if cond_A and cond_B and cond_C:
    print("Все числа кратны 3!")
else:
    print("Одно из или все числа не кратны 3!")