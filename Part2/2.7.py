def digit_sumcif(num: int) -> bool:
    if len(str(num)) != 4:
        raise NameError("Число не четырехзначное!")
    list_ = [int(i) for i in str(num)]

    if (int(list_[0]) + int(list_[1])) == (int(list_[2]) + int(list_[3])):
        return True
    else:
        return False


def digit_sum(num: int) -> bool:
    if len(str(num)) != 4:
        raise NameError("Число не четырехзначное!")
    list_ = [int(i) for i in str(num)]

    if sum(list_) % 7 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(digit_sumcif(1234))
    print(digit_sumcif(7777))
    print(digit_sum(1234))
    print(digit_sum(7777))