def solution(number):
    odd = 0
    even = 0
    while number > 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    print("Число четных цифр в числе: ", even)
    print("Число нечетных цифр в числе: ", odd)


if __name__ == '__main__':
    number = int(input("Введите положительное целое натуральное число: "))
    solution(number)

