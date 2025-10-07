from typing import Callable


def rounded_avg(q: int, r: int) -> str | int:
    if r < q:
        return -1

    def sum_range(x: int, y: int, acc: int) -> int:
        if x > y:
            return acc
        return sum_range(x + 1, y, acc + x)

    total_sum: int = sum_range(q, r, 0)
    count_diff: int = (r - q) + 1
    mean_val: float = total_sum / count_diff
    nearest_int: int = round(mean_val)
    binary_str: str = bin(nearest_int)[2:]
    return binary_str