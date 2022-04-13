number = int(input("Введите число для проверки: "))

cond_1 = 1 <= number // 1000 <= 9
cond_2 = number != 4999

if cond_1 and number != 4999:
    print("Число четырехзначное и не равно 4999")
else:
    print("Число не четырехзначное или равно 4999!")