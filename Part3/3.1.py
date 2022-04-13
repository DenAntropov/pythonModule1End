vl = int(input("Введите сумму вклада на счету: "))

if vl < 5000:
    input(vl * 1.2)
elif 5000 <= vl <= 10000:
    input(vl * 1.22)
else:
    input("Введите сумму не больше 10000")