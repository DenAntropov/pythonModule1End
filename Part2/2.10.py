print(input("Введем стороны треугольника"))
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

tri = (a + b + c) * (a + b - c) * (a + c - b) * (b + c - a)
kvad = 8 * min(a, b, c) ** 4

if tri > 0:
    if tri > kvad:
        print("Площадь треугольника больше")
    elif tri < kvad:
        print("Площадь квадрата больше")
    else:
        print("Площади фигур равны")
else:
    print("Треугольник не существует при данном условии")