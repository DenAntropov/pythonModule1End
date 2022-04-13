number_A = int(input("Введите число А: "))
number_B = int(input("Введите число B: "))

cond_A = number_A % 2
cond_B = number_B % 2

if cond_A == 0 and cond_B == 1:
    print("Число А четное!")
elif cond_A == 1 and cond_B ==0:
    print("Число В четное!")
elif cond_A == 0 and cond_B == 0:
    print("Оба числа четные!")
else:
    print("Оба числа нечетные!")