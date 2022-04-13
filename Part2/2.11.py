def task(num: int) -> bool:
    if len(str(num)) != 4:
        raise NameError("Число не четырехзначное!")
    list_digits = [int(digit) for digit in str(num)]

    return False if len(set(list_digits)) == len(list_digits) else True


if __name__ == "__main__":
    print("False означает, что в числе были найдены не одинаковые значение, т.е. его числа - уникальные.")
    print(task(1111))
    print(task(1234))
