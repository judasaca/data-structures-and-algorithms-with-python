from typing import List


def recursive_sum(items: List[float | int], position: int = 0) -> int | float:
    if position >= len(items):
        return 0
    return items[position] + recursive_sum(items, position + 1)


print(
    recursive_sum(
        [
            19,
            2,
        ]
    )
)
