print("Введите стороны треугольника")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
print("Полученный треугольник: ")
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        if a**2 < c**2 + b**2 and b**2 < a**2 + c**2 and c**2 < a**2 + b**2:
            print("Остроугольный")
    elif c >= a and c >= b:
        if c**2 == a**2 + b**2:
            print("Прямоугольный")
        elif c**2 < a**2 + b**2:
            print("Остроугольный")
        elif c**2 > a**2 + b**2:
            print("Тупоугольный")
    elif a >= b and a >= c:
        if a**2 == c**2 + b**2:
            print("Прямоугольный")
        elif a**2 < c**2 + b**2:
            print("Остроугольный")
        elif a**2 > c**2 + b**2:
            print("Тупоугольный")
    elif b >= a and b >= c:
        if b**2 == a**2 + c**2:
            print("Прямоугольный")
        elif b**2 < a**2 + c**2:
            print("Остроугольный")
        elif b**2 > a**2 + c**2:
            print("Тупоугольный")
    elif a == b >= c:
        if a**2 == c**2 + b**2 and b**2 == a**2 + c**2:
            print("Прямоугольный")
        elif a**2 < c**2 + b**2 and b**2 < a**2 + c**2:
            print("Остроугольный")
        elif a**2 > c**2 + b**2 and b**2 > a**2 + c**2:
            print("Тупоугольный")
    elif a == c >= b:
        if a**2 == c**2 + b**2 and c**2 == a**2 + b**2:
            print("Прямоугольный")
        elif a**2 < c**2 + b**2 and c**2 < a**2 + b**2:
            print("Остроугольный")
        elif a**2 > c**2 + b**2 and c**2 > a**2 + b**2:
            print("Тупоугольный")
    elif b == c >= a:
        if b**2 == a**2 + c**2 and c**2 == a**2 + b**2:
            print("Прямоугольный")
        elif b**2 < a**2 + c**2 and c**2 < a**2 + b**2:
            print("Остроугольный")
        elif b**2 > a**2 + c**2 and c**2 > a**2 + b**2:
            print("Тупоугольный")
else:
    print("Не может существовать!")