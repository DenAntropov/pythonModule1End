def print_table(n: int):
    matrix = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            row = matrix[i]
            row.append((i+1)*(j+1))

    for row_index in range(n):
        for col_index in range(n):
            print(f"{matrix[row_index][col_index]:2}", end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Введите n размер таблицы умножения (формата nxn): "))
    print_table(n)