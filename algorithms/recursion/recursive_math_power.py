def recursive_pow(x: int, n: int) -> int:
    if n <= 0:
        return 1
    return x * recursive_pow(x, n - 1)


print(recursive_pow(3, 2))
