number = int(input("Введите число для проверки: "))

list_1 = list(range(-137, 51))
list_2 = list(range(55, 123))

if number in list_1:
    print("Число находится в первом промежутке!")
elif number in list_2:
    print("Число находится во втором промежутке!")
else:
    print("Число не принадлежит ни одному из промежутков!")
    