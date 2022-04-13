def task_dv(num) -> bool:
    list_ = [int(i) for i in str(abs(num))]
    if 10 <= sum(list_) <= 99:
        return True
    else:
        return False


def task_tr(num) -> bool:
    list_ = [int(i) for i in str(abs(num))]
    mul_ = 1
    for num in list_:
        mul_ *= int(num)
    if len(str(mul_)) == 3:
        return True
    else:
        return False


if __name__ == "__main__":

    print(task_dv(12))
    print(task_dv(555))
    print(task_tr(-12))
    print(task_tr(-1495))
