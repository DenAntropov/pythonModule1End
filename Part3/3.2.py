def card():
    m = ["пики", "трефы", "бубны", "червы"]
    d = ["Валет", 'Дама', 'Король', 'Туз']
    mN = int(input("Номер масти: ")) - 1
    if mN > len(m):
        return False
    dN = int(input("Номер достоинства: "))
    if dN >= 15:
        return False
    if dN > 10:
        dn -= 11
        return ''.join([d[dN], ' ', m[mN]])
    else:
        return ''.join([str(dN), ' ', m[mN]])


print(card())
