def recursive_inverse(items: list, position: int = -1) -> list:
    """This recursion method has complexity O(n)=n"""
    if position < -len(items):
        return []
    return [items[position]] + recursive_inverse(items, position - 1)


def optimized_recursive_inverse(items: list, start: int, end: int) -> None:
    """This recursion method has complexity O(n)=n/2"""
    if start < end - 1:
        items[start], items[end - 1] = items[end - 1], items[start]
        optimized_recursive_inverse(items, start + 1, end - 1)


print(recursive_inverse([0, 1, 25, 3]))
prueba2 = [0, 1, 25, 3]
optimized_recursive_inverse(prueba2, start=0, end=len(prueba2))
print(prueba2)
