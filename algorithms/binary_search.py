def binary_search(
    data: list[int], target: int, low_limit: int, high_limit: int
) -> int | None:
    if low_limit > high_limit:
        return None
    mid_point = (low_limit + high_limit) // 2
    if data[mid_point] == target:
        return mid_point
    elif data[mid_point] > target:
        return binary_search(data, target, low_limit, mid_point - 1)
    else:
        return binary_search(data, target, mid_point + 1, high_limit)


data = [1, 3, 7, 10, 15, 54, 61]

print(binary_search(data, 13, 0, len(data)))
