def solution(n: int):
    # money = {"m1": 1,
    #     "m2": 2,
    #     "m4": 4,
    #     "m8": 8,
    #     "m16": 16,
    #     "m32": 32,
    #     "m64": 64
    #     }


    list_nominals = [64, 32, 16, 8, 4, 2, 1]
    wallet = {key: 0 for key in list_nominals}  # {n ** 2: 0 for key in range(8, -1, -1)}
    for key in wallet:
        print("Сумму можно разбить на", n // key, "купюр номиналом", key)
        n %= key


    # val_ = list(money.values())
    # print("Рассчет ведем по следующим ключам: ", val_)

    # for currency in money.values():
    #     print("Сумму можно разбить на", n // val_[6], "купюр номиналом", val_[6])
    #     n %= val_[6]
    #     print("Сумму можно разбить на", n // val_[5], "купюр номиналом", val_[5])
    #     n %= val_[5]
    #     print("Сумму можно разбить на", n // val_[4], "купюр номиналом", val_[4])
    #     n %= val_[4]
    #     print("Сумму можно разбить на", n // val_[3], "купюр номиналом", val_[3])
    #     n %= val_[3]
    #     print("Сумму можно разбить на", n // val_[2], "купюр номиналом", val_[2])
    #     n %= val_[2]
    #     print("Сумму можно разбить на", n // val_[1], "купюр номиналом", val_[1])
    #     n %= val_[1]
    #     print("Сумму можно разбить на", n // val_[0], "купюр номиналом", val_[0])
    #     n %= val_[0]
    #     if currency == 1:
    #         break


if __name__ == '__main__':
    n = int(input("Введите сумму для расчета: "))
    solution(n)

