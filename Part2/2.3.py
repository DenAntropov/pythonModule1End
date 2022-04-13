def is_palindrome_number(num: int) -> bool:
    if num < 0:
        raise NameError("Число отрицательное!")

    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":

    print(is_palindrome_number(1234))
    print(is_palindrome_number(1234321))