def task_pr(num) -> bool:
    list_ = [int(i) for i in str(abs(num))]
    b = 10
    mul_ = 1
    for num in list_:
        mul_ *= int(num)
    if mul_ > b:
        return True
    else:
        return False


def task_tr(num) -> bool:
    list_ = [int(i) for i in str(abs(num))]
    if sum(list_) % 3 == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    print(task_pr(12))
    print(task_pr(555))
    print(task_tr(-12))
    print(task_tr(-1495))