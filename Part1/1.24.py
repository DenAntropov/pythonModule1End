A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

cond_1 = A > 0
cond_2 = B > 0
cond_3 = C > 0

if cond_1:
    print(A ** 3)
else:
    A = 0
    print(A)

if cond_2:
    print(B ** 3)
else:
    B = 0
    print(B)

if cond_3:
    print(C ** 3)
else:
    C = 0
    print(C)



