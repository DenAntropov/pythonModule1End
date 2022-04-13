number = int(input("Введите двузначное число: "))

# Число вычисляем в формате XY
x = number // 10
y = number % 10

if 0 <= number <= 9 or number >= 100:
    print("Число не является двузначным")
elif x == 4 or x == 7 or y == 4 or y == 7:
    print("Цифра 4 или 7 входит в число")
else:
    print("Ни цифра 4 ни 7 не входят в число")
