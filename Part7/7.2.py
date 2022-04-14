def solution(n):
    for i in range(n):
        for j in range(n):
            if i * 4 + j * 2 == n:
                print("Возможно {} кроликов и {} гусей".format(i, j))


if __name__ == "__main__":
    n = 64
    solution(n)
