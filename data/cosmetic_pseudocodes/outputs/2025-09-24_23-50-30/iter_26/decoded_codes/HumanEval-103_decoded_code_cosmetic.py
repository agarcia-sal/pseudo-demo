from typing import Union


def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return "-1"

    def accumulate_sum(a: int, b: int, c: int) -> int:
        if a > b:
            return c
        return accumulate_sum(a + 1, b, c + a)

    total_sum: int = accumulate_sum(x, y, 0)
    count: int = (y - x) + 1
    mean_val: float = total_sum / count
    nearest_int: int = round(mean_val)
    bin_val: str = bin(nearest_int)
    return bin_val