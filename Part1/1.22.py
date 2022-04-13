A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

cond_1 = A > 0
cond_2 = B > 0
cond_3 = C > 0

print(A ** 2 if cond_1 else A)
print(B ** 2 if cond_2 else B)
print(C ** 2 if cond_3 else C)