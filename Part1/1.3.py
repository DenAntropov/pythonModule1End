number = int(input("Введите число для проверки: "))

cond_ = number // 100
if cond_ >= 1:
    print("Число трехзначное!")
else:
    print("Число не трехзначное!")
    