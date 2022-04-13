number = int(input("Введите число для проверки: "))

cond_1 = number % 2 == 0
cond_2 = number % 10 == 3

print("Число четное" if cond_1 else "Число нечетное")
print("Число оканчивается на 3" if cond_2 else "Число не оканчивается на 3")

