def solution(n):
    LEGS_RABBIT = 4
    LEGS_DUCKS = 2
    for rabbit in range(n):
        for ducks in range(n):
            if rabbit * LEGS_RABBIT + ducks * LEGS_DUCKS == n:
                print(f"Возможно {rabbit} кроликов и {ducks} гусей")  # todo f-string


if __name__ == "__main__":
    n = 64
    solution(n)
