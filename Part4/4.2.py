def list_(n: int, m: int) -> list:
    return [(n + m - i) for i in range(n + 1, m)]
    return len([i for i in range(n, m + 1)])

if __name__ == "__main__":
    print(list_(5, 20), "   ", len(list_(5, 20)))
